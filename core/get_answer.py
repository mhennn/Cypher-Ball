from request.requests_api import RequestAnswer

class GetAnswer:
    def __init__(self):
        self.request_answer = RequestAnswer()

    def get_answer(self):
        return self.request_answer.retrieve_answer()