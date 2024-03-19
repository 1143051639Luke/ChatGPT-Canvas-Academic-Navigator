import pandas as pd
import os
from openai import OpenAI


def generate_embeddings(input_datapath, output_folder, model="text-embedding-3-small"):
   # Load the dataset
   df = pd.read_csv(input_datapath, header = 0)
   df.columns = ['Text', 'Source', 'Type']
   # Assuming the CSV file already has 'Text' and 'Value' columns
   # If you need to rename columns, do it here based on the actual structure of your CSV

   # Setup the OpenAI client
   api_key = os.environ["OPENAI_API_KEY"]
   # api_key = "your key" 
   # If you don't have the API key stored in your environment variables, you can pass it directly to the OpenAI constructor

   client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", api_key))

   # Function to get embedding
   def get_embedding(text, model="text-embedding-3-large"):
      text = text.replace("\n", " ")
      return client.embeddings.create(input = ['text'], model=model).data[0].embedding

   # Apply the function to compute embeddings
   df['Value'] = df.Text.apply(lambda x: get_embedding(x, model = model))

   # Construct the output file path
   base_name = os.path.basename(input_datapath)  # Get the base file name
   file_name_without_ext = os.path.splitext(base_name)[0]  # Remove the extension
   output_file_name = file_name_without_ext + "_embed.csv"  # Append _embed and extension
   output_datapath = os.path.join(output_folder, output_file_name)  # Construct full path

   # Save the result to the new CSV file
   df.to_csv(output_datapath, index=False)


# Test and Example
generate_embeddings("Preprocessing/Data/Middle_csv/merged_testpdf.csv", "Preprocessing/Data/Embeded",  model="text-embedding-3-large")
