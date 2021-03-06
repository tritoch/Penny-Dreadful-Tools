import json

from flask import Flask

from price_grabber import price

SRV = Flask(__name__)

@SRV.route("/<card>/")
def cardprice(card):
    card = card.replace('-split-', '//')
    return json.dumps(price.info_cached(name=card))

def init():
    SRV.run(port=5800, host='0.0.0.0')
