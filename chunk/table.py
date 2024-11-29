import os
import re

def extract_tables_from_md(file_path):
    """Extract tables from a markdown file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Regular expression to match markdown tables
    table_pattern = re.compile(r'(?<=\n)(\|.*?\|(?:\n\|[-\s|:]+.*?)+)(?=\n)', re.DOTALL)
    tables = table_pattern.findall(content)
    return tables

def save_tables_to_file(tables, output_file):
    """Save extracted tables to an output file."""
    with open(output_file, 'w', encoding='utf-8') as file:
        for idx, table in enumerate(tables):
            file.write(f"TABLE {idx+1}\n")
            file.write(table.strip() + "\n\n")

def extract_all_md_tables(directory):
    """Extract all markdown tables from all `.md` files in the directory."""
    all_tables = []
    
    # Walk through the directory and find all markdown files
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                print(f"Extracting tables from: {file_path}")
                tables = extract_tables_from_md(file_path)
                all_tables.extend(tables)
    
    return all_tables

def main():
    # Specify the directory where your markdown files are stored
    directory = input("Enter the directory containing the Markdown files: ")
    
    # Extract all tables from the markdown files in the directory
    tables = extract_all_md_tables(directory)
    
    # Save the extracted tables to a new file
    if tables:
        output_file = os.path.join(directory, 'extracted_tables.md')
        save_tables_to_file(tables, output_file)
        print(f"Extracted tables saved to: {output_file}")
    else:
        print("No tables found in the markdown files.")

if __name__ == "__main__":
    main()
