import datetime
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    now = datetime.datetime.now()
    return f'Привет, сейчас! {now}'


@app.route('/search/<word>')
def search(word):
    return f"You say {word}"