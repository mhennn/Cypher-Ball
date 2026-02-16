import requests

BASE_URL = "http://127.0.0.1:8000"

class RequestAnswer:
    def __init__(self):
        self.response = requests.get(f"{BASE_URL}/message")

    def retrieve_answer(self):
        result = self.response.json()
        return result['answer']