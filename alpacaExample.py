import alpaca_trade_api as tradeapi

api = tradeapi.REST(
    key_id='REPLACEME',
    secret_key='REPLACEME',
    base_url='https://paper-api.alpaca.markets'
)

order = api.submit_order(
    symbol='AAPL',
    shares=10,
    side='buy',
    limit_price=190,
    time_in_force='day',
)
