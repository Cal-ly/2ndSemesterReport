import re
import csv

# Define a function to parse markdown text
def parse_markdown(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    pattern = r"### (\d+)\. User Story: (.+?)\n(.*?)\n\n\*\*Tasks:\*\*\n(.*?)\n\n\*\*Acceptance Criteria:\*\*\n(.*?)\n\n\*\*Estimering:\*\* (\d)"
    matches = re.findall(pattern, text, re.DOTALL)
    return matches

# Define a function to write to CSV
def write_csv(data, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Writing the header
        header = ["Card Name", "Card Description", "Labels", "Checklist", "Checklist item"]
        writer.writerow(header)
        
        for num, title, story, tasks, criteria, estimate in data:
            estimate_color = {1: '1 (subtle green)', 2: '2 (green)', 3: '3 (yellow)', 5: '5 (orange)', 8: '8 (red)'}
            card_name = f"US {num} {title.replace(' - ', ' ')}"
            writer.writerow([card_name, story, estimate_color[int(estimate)], '', ''])
            writer.writerow(['', '', '', 'Tasks', tasks.strip().replace('\n', '; ').replace('- ', '')])
            writer.writerow(['', '', '', 'Acceptance Criteria', criteria.strip().replace('\n', '; ').replace('*Givet*', 'Givet')])

# Name of the markdown file to be processed
markdown_file_name = "user_stories.md"

# Parse markdown and write to CSV
data = parse_markdown(markdown_file_name)
write_csv(data, 'output.csv')