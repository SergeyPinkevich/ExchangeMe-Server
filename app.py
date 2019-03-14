import json

import requests
from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route('/rates')
def hello_world():
    return requests.get("http://www.floatrates.com/daily/usd.json").text


@app.route('/countries')
def countries():
    with open('static/countries.json') as data:
        return jsonify(json.load(data))


if __name__ == '__main__':
    app.run()
