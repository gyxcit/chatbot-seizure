import pdfplumber, os

pdf_folder = 'data/pdf'
text_folder = 'data/text'
os.makedirs(text_folder, exist_ok=True)
for fname in os.listdir(pdf_folder):
    if fname.endswith('.pdf'):
        with pdfplumber.open(os.path.join(pdf_folder, fname)) as pdf:
            text = ''.join(page.extract_text() or '' for page in pdf.pages)
        out_path = os.path.join(text_folder, fname.replace('.pdf', '.txt'))
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(text)