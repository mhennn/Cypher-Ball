from flask import Flask, render_template, redirect, url_for, request
from core.get_answer import GetAnswer

flask_app = Flask(__name__)
retrieve_answer = GetAnswer()

@flask_app.route('/')
def home():
    return render_template('index.html')

@flask_app.route('/answer', methods=['POST'])
def show_answer():
    display_answer = retrieve_answer.get_answer()
    return render_template('answer.html', ball_answer=display_answer)

if __name__ == "__main__":
    flask_app.run(debug=True)