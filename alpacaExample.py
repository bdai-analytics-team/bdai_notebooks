import alpaca_trade_api as tradeapi
api = tradeapi.REST('PKTSHUKFX9XQEP9EZ4T2',
                    'je32eqYEJMCoL1aZ9glYleaTdwiGgnnTK1InwHOY')
#order = api.submit_order(
#    symbol='AAPL',
#    shares=10,
#    side='buy',
#    limit_price=189.95,
#    time_in_force='day',
#)

# Places a limit order
api.submit_order('AAPL',10,'buy','limit','gtc',189.95)

# Lists all open orders
orders = api.list_orders()
