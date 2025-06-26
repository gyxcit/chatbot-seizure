import os
import requests
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from pinecone import Pinecone, ServerlessSpec
import numpy as np
from numpy.linalg import norm

# Load environment variables
load_dotenv()
HF_TOKEN = os.getenv('HUGGINGFACE_API_TOKEN')
if not HF_TOKEN:
    raise ValueError("Define HUGGINGFACE_API_TOKEN in .env")

PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
PINECONE_ENV     = os.getenv('PINECONE_ENV', 'aws')
PINECONE_REGION  = os.getenv('PINECONE_REGION', 'us-east1-gcp')
INDEX_NAME       = os.getenv('PINECONE_INDEX', 'epilepsy-chatbot')

# Initialize Pinecone client
pc = Pinecone(api_key=PINECONE_API_KEY)
indexes = pc.list_indexes().names()
# Create index if it doesn't exist
if INDEX_NAME not in pc.list_indexes().names():
    pc.create_index(
        name=INDEX_NAME,
        dimension=768,
        metric='euclidean',
        spec=ServerlessSpec(
            cloud=PINECONE_ENV,
            region=PINECONE_REGION
        )
    )
# Connect to the index
index = pc.Index(INDEX_NAME)

# Embedding model for retrieval
t2v = SentenceTransformer('all-mpnet-base-v2')

# LLM inference configuration
MODEL_ID = 'mistralai/Mistral-7B-Instruct-v0.3'
API_URL  = f'https://api-inference.huggingface.co/models/{MODEL_ID}'
HEADERS  = {
    'Authorization': f'Bearer {HF_TOKEN}',
    'Content-Type': 'application/json'
}

class RagMistralModel:
    def __init__(self, top_k: int = 3, top_k_hist: int = 3, max_gen_tokens: int = 256):
        # Nombre de contexts Pinecone et tours historiques à récupérer
        self.top_k = top_k
        self.top_k_hist = top_k_hist
        self.max_gen_tokens = max_gen_tokens
        # Historique illimité
        self.history: list[tuple[str, str]] = []

    def retrieve(self, query_text: str) -> list[str]:
        """Retrieve top-k context chunks from Pinecone index."""
        q_emb = t2v.encode(query_text).tolist()
        resp = index.query(
            vector=q_emb,
            top_k=self.top_k,
            include_metadata=True
        )
        contexts = [match['metadata'].get('source_text', match['id']) for match in resp['matches']]
        return contexts

    def retrieve_history(self, question: str) -> list[str]:
        """
        Encode chaque couple (question, réponse) de l'historique,
        calcule la similarité cosinus et renvoie les plus pertinentes.
        """
        if not self.history:
            return []

        q_emb = t2v.encode(question)
        hist_embs = [t2v.encode(q_prev + " " + a_prev) for q_prev, a_prev in self.history]
        sims = [float(np.dot(q_emb, h) / (norm(q_emb) * norm(h))) for h in hist_embs]
        top_idxs = np.argsort(sims)[-self.top_k_hist:][::-1]
        return [
            f"Tour {i+1} – Q: {self.history[i][0]}\nR: {self.history[i][1]}"
            for i in top_idxs
        ]

    def build_prompt(self, contexts: list[str], question: str, history_snippets: list[str]) -> str:
        """Construct RAG prompt: historique, contextes Pinecone + question."""
        bloc_intro = (
            "Tu es un assistant expert en neurologie. "
            "Utilise uniquement les passages et l'historique ci-dessous pour répondre."
        )

        parts = [bloc_intro]
        if history_snippets:
            hist_block = "Historique pertinent :\n" + "\n\n".join(history_snippets)
            parts.append(hist_block)

        ctx_block = "\n\n".join(f"Contexte {i+1}:\n{c}" for i, c in enumerate(contexts))
        parts.append(ctx_block)

        parts.append(f"Question: {question}\nRéponse:")
        return "\n\n".join(parts)

    def generate(self, prompt: str) -> str:
        """Call Mistral inference API and return generated text."""
        payload = {
            'inputs': prompt,
            'parameters': {
                'max_new_tokens': self.max_gen_tokens,
                'return_full_text': False,
            }
        }
        # Debug: afficher le prompt complet
        print("--- DEBUG PROMPT START ---")
        print(prompt)
        print("--- DEBUG PROMPT END ---")

        res = requests.post(API_URL, headers=HEADERS, json=payload, timeout=60)
        res.raise_for_status()
        data = res.json()

        # Extraction du texte généré
        if isinstance(data, list) and 'generated_text' in data[0]:
            text = data[0]['generated_text'].strip()
        elif 'generated_text' in data:
            text = data['generated_text'].strip()
        else:
            raise ValueError(f"Unexpected response format: {data}")

        # Couper avant tout nouveau "Question:" si présent
        if "Question:" in text:
            text = text.split("Question:")[0].strip()
        return text

    def ask(self, question: str) -> str:
        """Full RAG pipeline: retrieve docs + history -> build prompt -> generate -> update history."""
        contexts = self.retrieve(question)
        history_snips = self.retrieve_history(question)
        prompt = self.build_prompt(contexts, question, history_snips)
        answer = self.generate(prompt)
        # Conserver l'échange
        self.history.append((question, answer))
        return answer

# Exemple d'utilisation
if __name__ == '__main__':
    model = RagMistralModel(top_k=3, top_k_hist=3, max_gen_tokens=250)

    q1 = "Quels sont les signes d'une crise d’épilepsie sur l'EMG ?"
    a1 = model.ask(q1)
    print("Réponse 1:", a1)

    q2 = "Comment réduire le bruit sur la mesure EDA ?"
    a2 = model.ask(q2)
    print("Réponse 2:", a2)
