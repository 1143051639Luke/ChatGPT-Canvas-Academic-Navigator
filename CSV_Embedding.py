from docx import Document
import openai
import pandas as pd
import numpy as np

def read_text_from_txt(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

text = read_text_from_txt('/Users/luke/Desktop/Canvas/test.txt')


openai.api_key = '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'

def text_to_embeddings(text):
    response = openai.Embedding.create(
        input=text,
        model="text-embedding-3-small"  # Or another model like "text-embedding-3-small"
    )
    return response['data'][0]['embedding']

embeddings = text_to_embeddings(text)



def save_embeddings_to_numpy(embeddings, filename):
    np.save(filename, np.array(embeddings))

# Example usage
save_embeddings_to_numpy(embeddings, 'embeddings.npy')


