import alpaca_trade_api as tradeapi

API_KEY = "PK1U84UG2RUCT4R6HQZ5"
API_SECRET = "baU//9pMyfMsb41P6Oppm7CHOucgYLDuJXIk8pKQ"
APCA_API_BASE_URL = "https://paper-api.alpaca.markets"

# company symbols
# quantity
# side = {buy, sell}
# typeW = {market, limit, limit_price, stop}
    # market = purchases at market price
    # limit = purhcases at specified price 
# time_force = {day, gtc, opg, cls, ioc, fok}
    # day = day order. available only when stock market is open
    # gtc = the order is good until canceled
    # opg = 
    # cls = 
    # ioc = 
    # fok = 
# price = price to purchase only used if typeW is limit (ie 20.50 = $20.50)

# required: symbol of company to purchase stock from, quantity to purchase, type of purchase, time_force, 
def buyStock(symbolCompany, quantity, typeW, time_force, price, API_KEY_buy, API_SECRET_buy, APCA_API_BASE_URL_buy, api_v = 'v2', buy = 'buy'): 
    # checks if limit_price argument is needed. 
    api = tradeapi.REST(API_KEY_buy, API_SECRET_buy, APCA_API_BASE_URL_buy, api_version=api_v)
    if (typeW=='limit' or typeW=='stop_limit'):
        api.submit_order(
            symbol = symbolCompany,
            qty = quantity, 
            side = buy, 
            type = typeW,
            time_in_force= time_force, 
            limit_price = price)
    # 
    else:
        api.submit_order(
            symbol = symbolCompany,
            qty = quantity, 
            side = buy, 
            type = typeW,
            time_in_force= time_force)
    return

# buyStock('AAPL', 10, 'market', 'day', 20.50, API_KEY, API_SECRET, APCA_API_BASE_URL)
