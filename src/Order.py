from enum import Enum
from src.InstructionQueue import Instruction, InstructionType

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

    
    # Method to convert an Order to a given instruction
    def to_instruction(self, instruction_type, new_value=None):
        
        # Convert to NEW_ORDER instruction
        if instruction_type == InstructionType.NEW_ORDER:
            return Instruction(instruction_type=InstructionType.NEW_ORDER, order=self)
        
        # Convert to CANCEL_ORDER instruction
        elif instruction_type == InstructionType.CANCEL_ORDER:
            return Instruction(instruction_type=InstructionType.CANCEL_ORDER, order=self)
        
        # Convert to UPDATE_PRICE instruction
        elif instruction_type == InstructionType.UPDATE_PRICE:
            if new_value:
                new_order = Order(order_id=self.id, side=self.side, quantity=self.quantity, order_type=self.type, price=new_value)
                return Instruction(instruction_type=InstructionType.UPDATE_PRICE, order=new_order)
            else:
                raise ValueError("New price must be provided for UPDATE_PRICE instruction")
            
        # Convert to UPDATE_QUANTITY instruction
        elif instruction_type == InstructionType.UPDATE_QUANTITY:
            if new_value:
                new_order = Order(order_id=self.id, side=self.side, quantity=new_value, order_type=self.type, price=self.price)
                return Instruction(instruction_type=InstructionType.UPDATE_QUANTITY, order=new_order)
            else:
                raise ValueError("New quantity must be provided for UPDATE_QUANTITY instruction")
    