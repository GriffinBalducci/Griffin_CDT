# utils/paper_trading.py

class PaperTrader:
    def __init__(self, initial_balance=500):
        self.initial_balance = initial_balance
        self.balance = initial_balance
        self.positions = {}  # Dictionary to store positions for each currency pair
        self.transaction_history = []

    def buy(self, symbol, price, amount):
        cost = price * amount

        if cost <= self.balance:
            self.balance -= cost

            if symbol not in self.positions:
                self.positions[symbol] = 0

            self.positions[symbol] += amount
            self.transaction_history.append(('buy', symbol, price, amount))
            print(f"Bought {amount} {symbol} at ${price} each")
        else:
            print(f"Insufficient funds to buy {symbol}")

    def sell(self, symbol, price, amount):
        if symbol in self.positions and self.positions[symbol] >= amount:
            revenue = price * amount
            self.balance += revenue
            self.positions[symbol] -= amount
            self.transaction_history.append(('sell', symbol, price, amount))
            print(f"Sold {amount} {symbol} at ${price} each")
        else:
            print(f"Not enough {symbol} to sell")

    def print_portfolio(self, current_price, symbol):
        position_value = self.positions.get(symbol, 0) * current_price # Default to 0 position if none found
        total_value = self.balance + position_value
        print(f"{symbol} - Balance: ${self.balance:.2f}, Position: {self.positions.get(symbol, 0):.4f}, Portfolio Value: ${total_value:.2f}")

