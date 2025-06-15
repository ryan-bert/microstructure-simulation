from collections import deque

class Trade:

    # Constructor for the Trade class
    def __init__(self, trade_id, buy_order_id, sell_order_id, price, quantity, timestamp):
        self.trade_id = trade_id
        self.buy_order_id = buy_order_id
        self.sell_order_id = sell_order_id
        self.price = price
        self.quantity = quantity
        self.timestamp = timestamp

class ExecutedTrades:

    # Constructor for the ExecutedTrades class
    def __init__(self):
        self.trades = deque()

    # Method to log a trade
    def log_trade(self, trade):
        self.trades.append(trade)

    # Method to retrieve mosst recent trade
    def get_last_trade(self):
        
        # Return the last trade if available
        if self.trades:
            return self.trades[-1]
        # No trades executed
        return None


    # Method to print the order book in a readable format
    def __str__(self):

        # Check if there are any executed trades
        if not self.trades:
            return "No executed trades."
        
        # Convert trades to string format
        lines = ["Executed Trades:"]
        for trade in self.trades:
            lines.append(f"Trade ID: {trade.trade_id}, Buy Order ID: {trade.buy_order_id}, "
                         f"Sell Order ID: {trade.sell_order_id}, Price: {trade.price}, "
                         f"Quantity: {trade.quantity}, Timestamp: {trade.timestamp}")

        # Join the lines into a single string
        return "\n".join(lines)