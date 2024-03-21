import os
from Preprocessing import csvMerger
from Preprocessing import pdfSpliter
from Preprocessing import wordSpliter




def fileEditer(originFolder, csvPlacementFolder):
    """
    Traverse all the files (PDF and Word) and folders in originFolder, convert all the files
    to csv using function pdfSpliter/wordSpliter and put them to csvPlacementFolder in Data dictionary.
    """
    # Traverse the originFolder
    for root, dirs, files in os.walk(originFolder):
        for filename in files:
            # Construct the full path to the file
            file_path = os.path.join(root, filename)

            # Determine the type of file and use the appropriate splitter function
            if filename.endswith('.pdf'):
                # Use pdfSpliter for PDF files
                pdfSpliter(file_path, csvPlacementFolder, extract_image=False)
            elif filename.endswith(('.doc', '.docx')):
                # Use wordSpliter for Word documents
                wordSpliter(file_path, csvPlacementFolder, extract_image=False)


    
def mergeAllCsvFiles(folderPath, outputFile):
    """
    Traverses the given folder_path to find all CSV files and merges them into a single CSV file
    located at output_file.
    """
    # Initialize an empty list to store paths of all CSV files found.
    csv_files = []

    # Traverse the folder.
    for filename in os.listdir(folderPath):
        if filename.endswith('.csv'):
            # Construct full file path and add it to the list.
            filepath = os.path.join(folderPath, filename)
            csv_files.append(filepath)
    
    # Use the CsvMerger function to merge all CSV files into the specified output file.
    csvMerger(folderPath, outputFile)




# Example usage:
folderPath = 'Data/CSV'
outputFile = 'Data/CSV_Merged/merged_csv.csv'
orginalPath = "Data\Orginal" # All file 
mergeAllCsvFiles(folder_path, output_file)