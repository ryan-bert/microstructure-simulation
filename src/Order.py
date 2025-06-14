from enum import Enum

class OrderType(Enum):
    MARKET = "Market"
    LIMIT = "Limit"

class Side(Enum):
    BUY = "Buy"
    SELL = "Sell"

class Order:

    def __init__(self, order_id, side, price, quantity, order_type):
        self.id = order_id
        self.side = side
        self.price = price
        self.quantity = quantity
        self.type = order_type