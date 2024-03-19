import os
from Preprocessing import csvMerger

orginal_path = "Data\Orginal" # All file 

def merge_all_csv_files(folder_path, output_file):
    """
    Traverses the given folder_path to find all CSV files and merges them into a single CSV file
    located at output_file.

    Args:
    folder_path (str): The path to the folder to search for CSV files.
    output_file (str): The path to the resulting merged CSV file.
    """
    # Initialize an empty list to store paths of all CSV files found.
    csv_files = []

    # Traverse the folder.
    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            # Construct full file path and add it to the list.
            filepath = os.path.join(folder_path, filename)
            csv_files.append(filepath)
    
    # Use the CsvMerger function to merge all CSV files into the specified output file.
    CsvMerger(csv_files, output_file)




# Example usage:
folder_path = 'Data/CSV'
output_file = 'Data/CSV_Merged/test.csv'
merge_all_csv_files(folder_path, output_file)

    
