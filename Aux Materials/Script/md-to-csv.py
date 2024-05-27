import re
import csv

# Define a function to parse markdown text
def parse_markdown(text):
    pattern = r"### (\d+)\. User Story: (.+?)\n(.*?)\n\n\*\*Tasks:\*\*\n(.*?)\n\n\*\*Acceptance Criteria:\*\*\n(.*?)\n\n\*\*Estimering:\*\* (\d)"
    matches = re.findall(pattern, text, re.DOTALL)
    return matches

# Define a function to write to CSV
def write_csv(data, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for num, title, story, tasks, criteria, estimate in data:
            estimate_color = {1: '1 (subtle green)', 2: '2 (green)', 3: '3 (yellow)', 5: '5 (orange)', 8: '8 (red)'}
            writer.writerow([f"US {num} - {title}", story, estimate_color[int(estimate)], '', ''])
            writer.writerow(['', '', '', 'Tasks', tasks.strip().replace('\n', '; ')])
            writer.writerow(['', '', '', 'Acceptance Criteria', criteria.strip().replace('\n', '; ')])

# Example Markdown content
markdown_content = """
### 1. User Story: Kunde - Produktgennemsyn
*Som* kunde, *Ønsker jeg* at kunne se butikkens portfølje i kategorier, *Med det formål* bedst at kunne vælge det produkt, der opfylder mit behov.

**Tasks:**
- Implementer Razor Page, der kan fremvise alle produkter i en udvalgt kategori.

**Acceptance Criteria:**
- *Givet* at en kunde vil se en bestemt produktkategori, *når* de leder efter et produkt der opfylder deres behov, *så* får de en tilsvarende afgrænset visning af produktkataloget.

**Estimering:** 3
"""

# Parse markdown and write to CSV
data = parse_markdown(markdown_content)
write_csv(data, 'output.csv')