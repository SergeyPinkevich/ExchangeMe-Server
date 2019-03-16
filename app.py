import json

import requests
from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route('/rates')
def hello_world():
    response = requests.get("http://www.floatrates.com/daily/usd.json")
    json_response = json.loads(response.text)
    formatted_json = {}
    for key in json_response:
        rate = json_response[key]['rate']
        formatted_json[key] = rate
    return json.dumps(formatted_json)


@app.route('/countries')
def countries():
    with open('static/countries.json') as data:
        return jsonify(json.load(data))


if __name__ == '__main__':
    app.run()
