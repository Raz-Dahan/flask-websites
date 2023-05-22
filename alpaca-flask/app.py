from flask import Flask
from flask import render_template
from requests import get
app = Flask(__name__)


@app.route("/")
def website():
    return render_template("index.html")

@app.route("/bitcoin")
def bitcoin():
    response = get("https://api.coindesk.com/v1/bpi/currentprice.json")
    return response.json()
