import ccxt

def connect_to_exchange(api_key, api_secret, exchange_name='binance'):
    exchange = getattr(ccxt, exchange_name)
    ({
        'apiKey': api_key,
        'secret': api_secret,
    })
    return exchange
