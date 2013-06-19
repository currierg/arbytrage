class Trade:
    def __init__(self, market_1, market_2, cash):
        self.cash = cash

        price1 = average(buy, cash, m_1.bids)
        price2 = average(buy, cash, m_2.bids)

        bit_1 = buy(cash, m_1.bids)
        bit_2 = buy(cash, m_2.bids)

        sold1 = sell(bit_1, m_2.asks)
        sold2 = sell(bit_2, m_1.asks)

        if sold2 > sold1:
            self.buying_market = m_1.name
            self.selling_market = m_2.name
        else:
            self.buying_market = m_2.name
            self.selling_market = m_1.name

        self.percentage_profit = max(((sold2 - cash) / cash)*100,((sold1 - cash) / cash)*100)
        self.total_bitcoins_bought = max(bit_2, bit_1)
        self.total_profit = max(sold1, sold2)

    @property
    def buying_market(self):
        return self.buying_market
    
    @property
    def selling_market(self):
        return self.selling_market

    @property
    def total_bitcoins_bought(self):
        return self.total_bitcoins_bought

    @property
    def starting_cash(self):
        return self.cash

    @property
    def total_profit(self):
        return self.total_profit

    @property
    def percentage_profit(self):
        return self.percentage_profit

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

