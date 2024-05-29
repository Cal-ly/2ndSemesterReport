import fitz

file_path = "C:/Users/Cal-l/Documents/GitHub/2ndSemesterReport/Report/report.pdf"
pdf_document = fitz.open(file_path)

exclude_pages = set(range(0, 9)) 
exclude_pages.update(range(len(pdf_document) - 102, len(pdf_document)))

included_text = []

for page_num in range(len(pdf_document)):
    if page_num not in exclude_pages:
        page = pdf_document.load_page(page_num)
        included_text.append(page.get_text())

full_text = " ".join(included_text)
character_count = len(full_text)

print(f"Character count excluding specified sections: {character_count}")