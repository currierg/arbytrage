import requests
import json

def get_depth():
    response = requests.get("http://data.mtgox.com/api/1/BTCUSD/depth/fetch")

    return response.json()

def depth(depth_data):
    
    bids, asks = [], []

    # get bids and asks, ordered
    for bid in depth_data['return']['bids']:
        bids.append(dict(price=bid['price'],amount=bid['amount']))

    bids.reverse() # high to low

    for ask in depth_data['return']['asks']:
        asks.append(dict(price=ask['price'],amount=ask['amount']))

    return bids, asks

