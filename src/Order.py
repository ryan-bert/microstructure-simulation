from enum import Enum
from InstructionQueue import Instruction, InstructionType

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

    # Method to convert the order to a NEW_ORDER instruction
    def to_new_order_instruction(self):
        return Instruction(instruction_type=InstructionType.NEW_ORDER, order=self)
    
    # Method to convert the order to a CANCEL_ORDER instruction
    def to_cancel_order_instruction(self):
        return Instruction(instruction_type=InstructionType.CANCEL_ORDER, order=self)
    
    # Method to convert the order to an UPDATE_PRICE instruction
    def to_update_price_instruction(self, new_price):

        # Create a copy of the order with updated price
        new_order = Order(order_id=self.id, side=self.side, quantity=self.quantity, order_type=self.type, price=new_price)
        return Instruction(instruction_type=InstructionType.UPDATE_PRICE, order=new_order)
    
    # Method to convert the order to an UPDATE_QUANTITY instruction
    def to_update_quantity_instruction(self, new_quantity):

        # Create a copy of the order with updated quantity
        new_order = Order(order_id=self.id, side=self.side, quantity=new_quantity, order_type=self.type, price=self.price)
        return Instruction(instruction_type=InstructionType.UPDATE_QUANTITY, order=new_order)