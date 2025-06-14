from enum import Enum

class OrderType(Enum):
    MARKET = "Market"
    LIMIT = "Limit"

class Side(Enum):
    BUY = "Buy"
    SELL = "Sell"

class Order:

    # Constructor for the Order class
    def __init__(self, order_id, side, quantity, order_type, price=None):
        self.id = order_id
        self.side = side
        self.quantity = quantity
        self.type = order_type
        self.price = price