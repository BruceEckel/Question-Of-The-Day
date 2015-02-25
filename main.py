import os
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import DailyQuestions
dummy = dict(first_question=DailyQuestions.QUESTIONS[0][0],
		second_question=DailyQuestions.QUESTIONS[0][1])

def create_app():
  app = Flask(__name__)
  Bootstrap(app)
  return app

app = create_app()

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/first_question")
def first_question():
    return render_template('first_question.html', questions = dummy)

@app.route("/second_question")
def second_question():
    return render_template('second_question.html', questions = dummy)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

