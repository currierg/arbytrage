import requests
import json

def get_depth():
    response = requests.get("https://btc-e.com/api/2/btc_usd/depth")

    return response.json()

def depth(depth_data):

    bids, asks = [], []

    # get bids and asks, ordered
    for bid in depth_data['bids']:
        bids.append(dict(price=bid[0],amount=bid[1]))

    bids.reverse() # high to low

    for ask in depth_data['asks']:
        asks.append(dict(price=ask[0],amount=ask[1]))

    return bids, asks