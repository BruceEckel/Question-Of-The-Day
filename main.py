import os
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import DailyQuestions


def create_app():
  app = Flask(__name__)
  Bootstrap(app)
  if not app.debug:
    import logging
    file_handler = logging.FileHandler('question.log')
    file_handler.setLevel(logging.WARNING)
    app.logger.addHandler(file_handler)
  return app

app = create_app()

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/first_question")
def first_question():
    return render_template('first_question.html',
		questions = DailyQuestions.todaysQuestion())

@app.route("/second_question")
def second_question():
    return render_template('second_question.html',
    	questions = DailyQuestions.todaysQuestion())

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

