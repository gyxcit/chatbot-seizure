# Nettoyer et segmenter
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

os.makedirs('data/chunks', exist_ok=True)
splitter = RecursiveCharacterTextSplitter(chunk_size=700, chunk_overlap=100)
for txt in os.listdir('data/text'):
    with open(os.path.join('data/text', txt), encoding='utf-8') as f:
        content = f.read()
    chunks = splitter.split_text(content)
    # Sauvegarder chaque chunk
    for i, chunk in enumerate(chunks):
        with open(f"data/chunks/{txt.replace('.txt', '')}_chunk{i}.md", 'w', encoding='utf-8') as cf:
            cf.write(chunk)
