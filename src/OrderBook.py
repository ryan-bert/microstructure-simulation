from sortedcontainers import SortedDict
from collections import deque
from src.Order import Side

class OrderBook:

    # Constructor for the OrderBook class (ordered by best price)
    def __init__(self):

        # Bids: descending, Asks: ascending
        self.bids = SortedDict(lambda x: -x)
        self.asks = SortedDict()
        # Quick lookup for price level and side
        self.order_lookup = {}


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

        # Track for fast lookup
        self.order_lookup[order.id] = (order.side, order.price)


    # Method to remove an order by its ID
    def remove_order(self, order_id):

        # Check if order_id exists in the lookup
        if order_id not in self.order_lookup:
            return None

        # Use map to get side and price
        side, price = self.order_lookup[order_id]
        book = self.bids if side == Side.BUY else self.asks

        # Retrievve the relevant queue of orders
        queue = book.get(price)
        if not queue:
            return None

        # Iterate through the queue to find and remove the order
        for i, order in enumerate(queue):

            # Delete the order if it matches the order_id
            if order.id == order_id:
                del queue[i]
                # If queue is empty, remove the price level
                if not queue:
                    del book[price]
                # Remove from lookup dictionary
                del self.order_lookup[order_id]
                # Found and removed
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
    
    # Method to print the order book
    def print_order_book(self):

        # Bids (With IDs and total quantity)
        print("Bids:")
        for price, orders in self.bids.items():
            total_qty = sum(order.quantity for order in orders)
            print(f"Price: {price}, Total Qty: {total_qty}, Orders: {[order.id for order in orders]}")
        
        # Asks (With IDs and total quantity)
        print("Asks:")
        for price, orders in self.asks.items():
            total_qty = sum(order.quantity for order in orders)
            print(f"Price: {price}, Total Qty: {total_qty}, Orders: {[order.id for order in orders]}")