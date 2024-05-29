import fitz  # PyMuPDF

# Load the PDF file
file_path = "report/report.pdf"
pdf_document = fitz.open(file_path)

# Define the page ranges to exclude:
# Adjust the range based on actual document structure
exclude_pages = set(range(0, 2))  # Exclude first 2 pages (title page, table of contents)
exclude_pages.update(range(len(pdf_document) - 10, len(pdf_document)))  # Exclude last 10 pages (bibliography, appendices)

# Initialize variables to hold text content
included_text = []

# Iterate through the pages and extract text
for page_num in range(len(pdf_document)):
    if page_num not in exclude_pages:
        page = pdf_document.load_page(page_num)
        included_text.append(page.get_text())

# Join the text content and count the characters
full_text = " ".join(included_text)
character_count = len(full_text)

print(f"Character count excluding specified sections: {character_count}")