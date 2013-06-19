import btce
import mtgox

def _depth(market_data):

   depth_data = market_data

   # get bids and asks, ordered
   bids = depth_data['return']['bids'] 
   bids.reverse() # high to low
   asks = depth_data['return']['asks'] # low to high
 
   return bids, asks