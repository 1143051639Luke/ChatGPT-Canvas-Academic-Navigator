import pandas as pd
import os
from openai import OpenAI



input_datapath = "Data/testpdf1.csv"  #Should be csv file with "Text" and "Value" columns
df = pd.read_csv(input_datapath, header = 0)
df = df.rename({'0': 'Text', '1': 'Source', '2': 'Type'}, axis='columns')

api_key = os.environ["OPENAI_API_KEY"]
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", api_key))

def get_embedding(text, model="text-embedding-3-large"):
   text = text.replace("\n", " ")
   return client.embeddings.create(input = ['text'], model=model).data[0].embedding

df['Value'] = df.Text.apply(lambda x: get_embedding(x, model='text-embedding-3-small'))
df.to_csv('Output/testpdf1_embed.csv', index=False)