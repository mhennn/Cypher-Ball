from fastapi import FastAPI
import random
from word_list import WORDS

app = FastAPI(debug=True)

@app.get('/')
def home():
    return "Welcome to Cyper-Ball API"

@app.get('/message')
def give_answer():
    random_answer = random.choice(WORDS)
    return {
        "answer": random_answer
    }