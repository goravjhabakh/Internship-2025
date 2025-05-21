import pdfplumber

#pdf_path = '../docs/Key Remote Working Guidelines - Playbook.pdf'
pdf_path = '../docs/Holiday Schedule 2025.pdf'
output_path = 'extracted_table.txt'

with pdfplumber.open(pdf_path) as pdf, open(output_path, 'w', encoding='utf-8') as f:
    for pg_num,page in enumerate(pdf.pages, start=1):
        text = page.extract_text()
        tables = page.extract_tables()

        f.write(f'Page Number: {pg_num}\n')
        f.write(f'Text: \n{text}\n')
        f.write(f'Tables: \n{tables}\n\n')

pdf_path = '../docs/Key Remote Working Guidelines - Playbook.pdf'
output_path = 'extracted_text.txt'

with pdfplumber.open(pdf_path) as pdf, open(output_path, 'w', encoding='utf-8') as f:
    for pg_num,page in enumerate(pdf.pages, start=1):
        text = page.extract_text()
        tables = page.extract_tables()

        f.write(f'Page Number: {pg_num}\n')
        f.write(f'Text: \n{text}\n')
        f.write(f'Tables: \n{tables}\n\n')