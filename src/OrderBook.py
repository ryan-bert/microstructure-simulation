from sortedcontainers import SortedDict
from collections import deque
from src.Order import Side

class OrderBook:

    # Constructor for the OrderBook class (ordered by best price)
    def __init__(self, ticker):
        self.ticker = ticker
        self.bids = SortedDict(lambda x: -x)      # Bids: descending
        self.asks = SortedDict()                  # Asks: ascending


    # Method to add an order to the order book
    def add_order(self, order):

        # Determine whether to use bid or ask book
        if order.side == Side.BUY:
            book = self.bids
        elif order.side == Side.SELL:
            book = self.asks
        else:
            raise ValueError("Order side must be either BUY or SELL")

        # Create an empty deque if price level has no orders
        if order.price not in book:
            book[order.price] = deque()
        
        # Add order to the end of appropriate queue (FIFO)
        book[order.price].append(order)


    def remove_order(self, order_id):
        
        # Iterate over each order, within each price level
        for book in [self.bids, self.asks]:
            for price in list(book.keys()):
                queue = book[price]
                for i, order in enumerate(queue):

                    # Check if the order ID matches
                    if order.id == order_id:
                        # Remove the order from the queue
                        del queue[i]
                        # If queue is empty, remove the price level
                        if not queue:
                            del book[price]
                        # Found
                        return True
        # Not found
        return False