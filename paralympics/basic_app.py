from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route("/<string:name>")
def hello(name):
    return f"Hello, {escape(name)} and welcome to my paralympics app"

@app.route('/')
def index():
    return render_template('index.html')

    

if __name__ == '__main__':
    app.run(debug=True)
