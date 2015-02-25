import os
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

def create_app():
  app = Flask(__name__)
  Bootstrap(app)
  return app

app = create_app()

@app.route("/")
def index():
    #return "<h1>hello, world</h1>"
    return render_template('index.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

