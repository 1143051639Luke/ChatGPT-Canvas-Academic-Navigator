from langchain_community.document_loaders import PyPDFLoader
import pandas as pd
import os


# loader = PyPDFLoader("Data/testpdf.pdf")
# pages = loader.load_and_split()

# df = pd.DataFrame(pages)
# df.to_csv('Output/testpdf.csv', index=False)


def spliter(pdf_path, output_folder, edtract_image = False):
    """
    This function takes a PDF file path and outputs a CSV file containing the text of each page of the PDF.

    Parameters:
    - pdf_path: str, the path to the input PDF file.
    - csv_path: str, the path where the output CSV file should be saved.
    """
    loader = PyPDFLoader(pdf_path, extract_images = edtract_image)
    pages = loader.load_and_split()
    
    # Creating a DataFrame with the loaded pages
    df = pd.DataFrame(pages)
    
    # Getting the name of the PDF file
    base_name = os.path.basename(pdf_path)
    name, ext = os.path.splitext(base_name)
    csv_filename = f"{name}.csv"
    output_folder = os.path.join(output_folder, csv_filename)

    # Saving the DataFrame to a CSV file
    df.to_csv(output_folder, index=False)

# Test and Example
spliter("Preprocessing/Data/Orginal/CPSC320.pdf","Preprocessing/Data/Middle_csv")