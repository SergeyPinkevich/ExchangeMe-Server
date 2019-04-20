import json

import requests
from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)


@app.route('/rates')
def rates():
    response = requests.get("http://www.floatrates.com/daily/usd.json")
    json_response = json.loads(response.text)
    rates_list = []
    rates_list.insert(0, {"currency": "USD", "rate": 1.0})
    i = 1
    for key in json_response:
        rate = json_response[key]['rate']

        formatted_json = {"currency": str(key).upper(), "rate": rate}
        rates_list.insert(i, formatted_json)
        i += 1
    response = {"rates": rates_list}
    return json.dumps(response)


@app.route('/countries')
def countries():
    if "Accept-Language" in request.headers:
        languages = request.headers["Accept-Language"]
    else:
        languages = "en-EN"
    if "RU" in languages:
        file_name = 'static/countries-ru.json'
    else:
        file_name = 'static/countries-en.json'
    with open(file_name) as data:
        return jsonify(json.load(data))


if __name__ == '__main__':
    app.run()
