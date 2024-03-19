import os
import csv
import pandas as pd
import docx

def split_word(docx_path,output_folder):
    doc = docx.Document(docx_path)
    
    pages = []
    
    for paragraph in doc.paragraphs:
        pages.append(paragraph.text)
        
    df = pd.DataFrame({'Text': pages})
    # df['Source'] = docx_path
    # df['Type'] = 'WordDocument'
    
    base_name = os.path.basename(docx_path)
    name, ext = os.path.splitext(base_name)
    csv_filename = f"{name}.csv"
    output_path = os.path.join(output_folder, csv_filename)
    
    df.to_csv(output_path, index=False)   
    
# Test and Examples
split_word("Preprocessing/Data/Origin/word1.docx","Preprocessing/Data/Middle_csv") 



