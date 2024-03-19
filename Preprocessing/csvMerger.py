import pandas as pd


def CsvMerger(csv_files, output_file):
    
    # Create an empty DataFrame to store the merged data
    merged_data = pd.DataFrame()
    
    # Iterate over each CSV file
    for file in csv_files:
        # Read the CSV file into a DataFrame
        data = pd.read_csv(file)
        
        merged_data = pd.concat([merged_data, data])
        # Append the data to the merged_data DataFrame
        # merged_data = merged_data.append(data, ignore_index=True)
    
    # Write the merged data to a new CSV file
    merged_data.to_csv(output_file, index=False)

# Test and Example
CsvMerger(["Preprocessing/Data/Middle_csv/testpdf_1.csv", "Preprocessing/Data/Middle_csv/testpdf_2.csv"], "Preprocessing/Data/Middle_csv/merged_testpdf.csv")