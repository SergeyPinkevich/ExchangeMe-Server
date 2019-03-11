from flask import Flask
import requests

app = Flask(__name__)


@app.route('/rates')
def hello_world():
    return requests.get("http://www.floatrates.com/daily/usd.json").text


if __name__ == '__main__':
    app.run()
