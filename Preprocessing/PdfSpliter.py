from langchain_community.document_loaders import PyPDFLoader
import pandas as pd


# loader = PyPDFLoader("Data/testpdf.pdf")
# pages = loader.load_and_split()

# df = pd.DataFrame(pages)
# df.to_csv('Output/testpdf.csv', index=False)


def spliter(pdf_path, csv_path):
    """
    This function takes a PDF file path and outputs a CSV file containing the text of each page of the PDF.

    Parameters:
    - pdf_path: str, the path to the input PDF file.
    - csv_path: str, the path where the output CSV file should be saved.
    """
    loader = PyPDFLoader(pdf_path)
    pages = loader.load_and_split()
    
    # Creating a DataFrame with the loaded pages
    df = pd.DataFrame(pages, columns=['Page Text'])
    
    # Saving the DataFrame to a CSV file
    df.to_csv(csv_path, index=False)