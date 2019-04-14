import json

import requests
from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route('/rates')
def rates():
    response = requests.get("http://www.floatrates.com/daily/usd.json")
    json_response = json.loads(response.text)
    rates_list = []
    rates_list.insert(0, {"code": "USD", "rate": 1.0})
    i = 1
    for key in json_response:
        rate = json_response[key]['rate']

        formatted_json = {"code": str(key).upper(), "rate": rate}
        rates_list.insert(i, formatted_json)
        i += 1
    return json.dumps(rates_list)


@app.route('/countries')
def countries():
    with open('static/countries.json') as data:
        return jsonify(json.load(data))


if __name__ == '__main__':
    app.run()
