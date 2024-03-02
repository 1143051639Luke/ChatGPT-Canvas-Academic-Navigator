# imports
import openai
import ast  # for converting embeddings saved as strings back to arrays
from openai import OpenAI # for calling the OpenAI API
import pandas as pd  # for storing text and embeddings data
import tiktoken  # for counting tokens
import os # for getting API token from env variable OPENAI_API_KEY
from scipy import spatial  # for calculating vector similarities for search

# models
EMBEDDING_MODEL = "text-embedding-ada-002"
GPT_MODEL = "gpt-4-0125-preview"

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "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"))

# download pre-chunked text and pre-computed embeddings
# this file is ~200 MB, so may take a minute depending on your connection speed
embeddings_path = "/Users/luke/Desktop/Canvas/test2.csv"

df = pd.read_csv(embeddings_path)
#print(df.columns)

# convert embeddings from CSV str type back to list type
df['Value'] = df['Value'].apply(ast.literal_eval)


# search function
def strings_ranked_by_relatedness(
    query: str,
    df: pd.DataFrame,
    relatedness_fn=lambda x, y: 1 - spatial.distance.cosine(x, y),
    top_n: int = 100
) -> tuple[list[str], list[float]]:
    """Returns a list of strings and relatednesses, sorted from most related to least."""
    query_embedding_response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=query,
    )
    query_embedding = query_embedding_response.data[0].embedding
    strings_and_relatednesses = [
        (row["Text"], relatedness_fn(query_embedding, row["Value"]))
        for i, row in df.iterrows()
    ]
    strings_and_relatednesses.sort(key=lambda x: x[1], reverse=True)
    strings, relatednesses = zip(*strings_and_relatednesses)
    return strings[:top_n], relatednesses[:top_n]

def num_tokens(text: str, model: str = GPT_MODEL) -> int:
    """Return the number of tokens in a string."""
    encoding = tiktoken.encoding_for_model(model)
    return len(encoding.encode(text))


def query_message(
    query: str,
    df: pd.DataFrame,
    model: str,
    token_budget: int
) -> str:
    """Return a message for GPT, with relevant source texts pulled from a dataframe."""
    strings, relatednesses = strings_ranked_by_relatedness(query, df)
    introduction = 'Use the below articles on the 2022 Winter Olympics to answer the subsequent question. If the answer cannot be found in the articles, write "I could not find an answer."'
    question = f"\n\nQuestion: {query}"
    message = introduction
    for string in strings:
        next_article = f'\n\nWikipedia article section:\n"""\n{string}\n"""'
        if (
            num_tokens(message + next_article + question, model=model)
            > token_budget
        ):
            break
        else:
            message += next_article
    return message + question


def ask(
    query: str,
    df: pd.DataFrame = df,
    model: str = GPT_MODEL,
    token_budget: int = 4096 - 500,
    print_message: bool = False,
) -> str:
    """Answers a query using GPT and a dataframe of relevant texts and embeddings."""
    message = query_message(query, df, model=model, token_budget=token_budget)
    if print_message:
        print(message)
    messages = [
        {"role": "system", "content": "You answer questions about the 2022 Winter Olympics."},
        {"role": "user", "content": message},
    ]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0
    )
    response_message = response.choices[0].message.content
    return response_message

question = "Base on the text I gave to you, who study in UBC?"
answer = ask(query=question)
print("Answer:", answer)


