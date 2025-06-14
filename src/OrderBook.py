from sortedcontainers import SortedDict
from collections import deque
from src.Order import Side

class OrderBook:

    # Constructor for the OrderBook class (ordered by best price)
    def __init__(self):
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


    # Method to remove an order by its ID
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
                        return order
        # Not found
        return None

    
    # Method to update the price of an order
    def update_order_price(self, order_id, new_price):

        # Remove and retrieve the order
        order = self.remove_order(order_id)

        # If order was found, update its price and re-add it
        if order:
            order.price = new_price
            self.add_order(order)
            return order

        # Order not found
        return None


    # Method to update the quantity of an order
    def update_order_quantity(self, order_id, new_quantity):

        # Remove and retrieve the order
        order = self.remove_order(order_id)

        # If order was found, update its quantity and re-add it
        if order:
            order.quantity = new_quantity
            self.add_order(order)
            return order

        # Order not found
        return None