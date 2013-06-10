import requests
# from common.constants import EXCHANGES
# import BeautifulSoup
import json

def depth(market):

   response = requests.get(market)

   depth_data = response.json() #json.load(response.text)

   # get bids and asks, ordered
   bids = depth_data['return']['bids'] 
   bids.reverse() # high to low
   asks = depth_data['return']['asks'] # low to high

   # print "high buying price: ", bids[0]['price']
   # print "low selling price: ", asks[0]['price']

   return bids, asks


def buy(cash, depth):
    bitcoins = 0

    for order in depth:
        if cash > order['price'] * order['amount']:
            cash -= order['price'] * order['amount']
            bitcoins += order['amount']
        else:
            
            bitcoins += cash / order['price']
            break

    return bitcoins


def sell(bitcoins, depth):
    cash = 0

    for order in depth:
        if bitcoins > order['amount']:
            bitcoins -= order['amount']
            cash += order['amount'] * order['price']
        else:
            
            cash += bitcoins * order['price']
            break

    return cash

def average(action, amount, depth):
    if action == buy:
        return amount / buy(amount, depth)
    elif action == sell:
        return sell(amount, depth) / amount
    else:
        return -1