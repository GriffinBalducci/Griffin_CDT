from utils.api_connector import connect_to_exchange, place_order
from utils.bar_fetcher import fetch_data
#from strategies.moving_average import moving_average_crossover
from utils.paper_trader import PaperTrader

# Configurations
SYMBOLS = ['BTC/USDT', 'ETH/USDT', 'XRP/USDT']
TIMEFRAME = '5m'

def main():
    # Initialize PaperTrader
    trader = PaperTrader(initial_balance=10000)

    # Loop through each symbol to simulate trades
    for symbol in SYMBOLS:
        print(f"Trading {symbol}...")

        # Fetch market data for the current symbol
        exchange = connect_to_exchange('your_api_key', 'your_api_secret', 'binance')
        data = fetch_data(exchange, symbol, TIMEFRAME)
        
        # Extract close prices for strategy
        close_prices = [d[4] for d in data]

        # Get trading signal
        signal = moving_average_crossover(close_prices)

        # Simulate the order placement based on signal
        if signal == 'buy':
            trader.buy(symbol, close_prices[-1], 0.01)  # Buy 0.01 of the asset
        elif signal == 'sell':
            trader.sell(symbol, close_prices[-1], 0.01)  # Sell 0.01 of the asset
        
        # Print the portfolio status for the current symbol
        trader.print_portfolio(close_prices[-1], symbol)

if __name__ == "__main__":
    main()
