import os
from docx import Document
import fitz  # PyMuPDF

def read_docx_content(filepath):
    """Extract text from a Word document"""
    doc = Document(filepath)
    return '\n'.join([para.text for para in doc.paragraphs])

def read_pdf_content(filepath):
    """Extract text from a PDF document"""
    doc = fitz.open(filepath)
    return '\n'.join([page.get_text() for page in doc])

def process_folder(folder_path):
    """Process all PDF and Word documents in the specified folder"""
    all_texts = []  # List to hold texts from all documents
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            filepath = os.path.join(root, filename)
            if filename.endswith('.docx'):
                all_texts.append(read_docx_content(filepath))
            elif filename.endswith('.pdf'):
                all_texts.append(read_pdf_content(filepath))
    return "\n\n".join(all_texts)

def save_text_to_file(text, output_filepath):
    """Save the combined text to a new text file"""
    with open(output_filepath, 'w', encoding='utf-8') as file:
        file.write(text)

# Set the path to your folder and output file
folder_path = '/Users/luke/Desktop/Canvas/Test folder'
output_filepath = 'test.txt'

# Process the folder and save the combined text to a file
combined_text = process_folder(folder_path)
save_text_to_file(combined_text, output_filepath)

print(f"Combined text has been saved to {output_filepath}")