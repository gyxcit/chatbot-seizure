#!/usr/bin/env python3
import os, sys, requests
from dotenv import load_dotenv

load_dotenv()
HF_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")
if not HF_TOKEN:
    sys.exit("Erreur : définis HF_TOKEN dans ton .env (il doit commencer par hf_)")

MODEL_ID = "mistralai/Mistral-7B-Instruct-v0.3"
API_URL  = f"https://api-inference.huggingface.co/models/{MODEL_ID}"
HEADERS  = {
    "Authorization": f"Bearer {HF_TOKEN}",
    "Content-Type": "application/json"
}

# 1. Vérifier l'endpoint
try:
    r = requests.head(API_URL, headers=HEADERS, timeout=10)
    r.raise_for_status()
    print("✅ Endpoint OK (200)")
except Exception as e:
    sys.exit(f"❌ Impossible d'atteindre {API_URL} : {e}")

# 2. Envoi du prompt
def query(prompt, max_tokens=256):
    payload = {
        "inputs": prompt,
        "parameters": {"max_new_tokens": max_tokens}
    }
    r = requests.post(API_URL, headers=HEADERS, json=payload, timeout=60)
    r.raise_for_status()
    return r.json()

if __name__ == "__main__":
    prompt = "Explique le rôle de l'accéléromètre dans la détection d'une crise épileptique."
    resp = query(prompt)
    # Extraire le texte généré
    if isinstance(resp, list) and "generated_text" in resp[0]:
        print(resp[0]["generated_text"])
    elif isinstance(resp, dict) and "generated_text" in resp:
        print(resp["generated_text"])
    else:
        print(resp)
