from enum import Enum
from collections import deque
from time import time

class InstructionType(Enum):
    NEW_ORDER = "New Order"
    CANCEL_ORDER = "Cancel Order"
    UPDATE_ORDER = "Update Order"

class Instruction:

    # Constructor for the Instruction class
    def __init__(self, instruction_type, order):
        self.processed_timestamp = None     # Set by engine
        self.type = instruction_type
        self.order = order

class InstructionQueue:

    # Constructor for the InstructionQueue class
    def __init__(self):
        self.active_instructions = deque()
        self.processed_instructions = deque()

    
