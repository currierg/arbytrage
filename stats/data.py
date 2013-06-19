import json
from datetime import datetime

import markets

def record(market_list, depth_list, filename=None):

    if not filename:
        filename = str(datetime.utcnow())

    with open(filename, "w+")as fp:
        output = ""
        for market, depth in zip(market_list, depth_list):
            output += json.dumps({market: depth})

        fp.write(output)

def collect():
    market_list = [fn for fn in dir(markets) if "_" not in fn]
    depth_list = []

    for m in market_list:
        market = getattr(markets, m)

        depth_list.append(market.get_depth())

    return market_list, depth_list




