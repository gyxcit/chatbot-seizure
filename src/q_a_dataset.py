import os, random, csv



chunks = sorted(os.listdir('data/chunks'))
sample = random.sample(chunks, min(50, len(chunks)))

with open('data/validation_template.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['chunk_id', 'text_snippet', 'question', 'reference_answer'])
    for fname in sample:
        text = open(os.path.join('data/chunks', fname), encoding='utf-8').read()
        snippet = text[:200].replace('\n', ' ') + '…'
        writer.writerow([fname, snippet, '', ''])
print("validation_template.csv généré.")
