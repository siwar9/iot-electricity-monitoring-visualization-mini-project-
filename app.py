from flask import Flask,render_template,url_for,request,redirect, make_response
import random
import json
from time import time
from random import random
from flask import Flask, render_template, make_response
app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def main():
    return render_template('index.html')


@app.route('/data', methods=["GET", "POST"])
def data():
    # Format du data
    # [TIME, Electricity]

    Electricity = random() /1.25  #random donne par défaut une valeur aléatoire entre 0 et 1 et 1/1.25 = 0.8 (la consommation moyene d'electricité)

    data = [time() * 1000, Electricity]

    response = make_response(json.dumps(data))

    response.content_type = 'application/json'

    return response


if __name__ == "__main__":
    app.run(debug=True)