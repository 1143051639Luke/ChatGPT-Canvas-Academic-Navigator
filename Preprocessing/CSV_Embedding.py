import pandas as pd
import os
from openai import OpenAI



input_datapath = "Data/test2.csv"  #Should be csv file with "Text" and "Value" columns
df = pd.read_csv(input_datapath)
df = df[["Text","Value"]]

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "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"))

def get_embedding(text, model="text-embedding-3-large"):
   text = text.replace("\n", " ")
   return client.embeddings.create(input = [text], model=model).data[0].embedding

df['Value'] = df.Text.apply(lambda x: get_embedding(x, model='text-embedding-3-small'))
df.to_csv('output/test2_embed.csv', index=False)