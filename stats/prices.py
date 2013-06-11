import requests
# from common.constants import EXCHANGES
# import BeautifulSoup
import json

def depth_mtgox():
    response = requests.get("http://data.mtgox.com/api/1/BTCUSD/depth/fetch")

    depth_data = response.json() #json.load(response.text)

    bids, asks = [], []

    # get bids and asks, ordered
    for bid in depth_data['return']['bids']:
        bids.append(dict(price=bid['price'],amount=bid['amount']))

    bids.reverse() # high to low

    for ask in depth_data['return']['asks']:
        asks.append(dict(price=ask['price'],amount=ask['amount']))

    return bids, asks

def depth_btce():
    response = requests.get("https://btc-e.com/api/2/btc_usd/depth")

    depth_data = response.json() #json.load(response.text)

    bids, asks = [], []

    # get bids and asks, ordered
    for bid in depth_data['bids']:
        bids.append(dict(price=bid[0],amount=bid[1]))

    bids.reverse() # high to low

    for ask in depth_data['asks']:
        asks.append(dict(price=ask[0],amount=ask[1]))

    return bids, asks

def formulate_trade(m_1, m_2, cash):

    price1 = average(buy,cash,m_1['bids'])
    price2 = average(buy,cash,m_2['bids'])

    print "Buy market1: ", price1
    print "Buy market2: ", price2

    bit_1 = buy(cash, m_1['bids'])
    bit_2 = buy(cash, m_2['bids'])

    sold1 = sell(bit_1, m_2['asks'])
    sold2 = sell(bit_2, m_1['asks'])

    print "Sell market1 to m2: ", sold1
    print "Sell market2 to m1", sold2

    if sold2 > sold1:
        print "Percent profit: ", ((sold2 - cash) / cash)*100 
    else:
        print "Percent profit: ", ((sold1 - cash) / cash)*100


def depth(market):

   response = requests.get(market)

   depth_data = response.json() #json.load(response.text)

   # get bids and asks, ordered
   bids = depth_data['return']['bids'] 
   bids.reverse() # high to low
   asks = depth_data['return']['asks'] # low to high
 
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