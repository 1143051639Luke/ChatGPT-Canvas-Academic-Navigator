
import requests

class ChatGPTAPI:
    def __init__(self, api_url, access_token):
        self.api_url = api_url
        self.headers = {'Authorization': f'Bearer {access_token}'}

    def process_query(self, query):
        data = {'prompt': query, 'max_tokens': 50}
        response = requests.post(self.api_url, headers=self.headers, json=data)
        if response.status_code == 200:
            return response.json()
        else:
            return {'error': 'Failed to process query'}
