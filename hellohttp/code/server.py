import datetime
from flask import Flask
from flask import request

import gunicorn
from hellohttp.code.card_game import main
app = Flask(__name__)


@app.route('/')
def hello_world():
    num_players = request.args.get('num_players', None)
    now = datetime.datetime.now()
    player = main()
    return {
        "first_layer": player
    }
    # return f'Привет, сейчас! {now}'


@app.route('/search/<word>')
def search(word):
    return f"You say {word}"


if __name__ == '__main__':
    app.run(host='localhost', port=8080)
