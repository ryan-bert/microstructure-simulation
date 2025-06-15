from enum import Enum
from collections import deque
from time import time

class InstructionType(Enum):

    # Define the types of instructions
    NEW_ORDER = "New Order"
    CANCEL_ORDER = "Cancel Order"
    UPDATE_PRICE = "Update Price"
    UPDATE_QUANTITY = "Update Quantity"

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


    # Method to add an instruction to the queue
    def add_instruction(self, instruction):
        self.active_instructions.append(instruction)


    # Method to check if the queue is empty
    def is_empty(self):
        return len(self.active_instructions) == 0


    # Method to process the next instruction in the queue
    def process_next_instruction(self):

        # Check if there are any active instructions
        if not self.active_instructions:
            return None
        
        # Pop the next instruction from the queue
        instruction = self.active_instructions.popleft()

        # Record the time and mark as processed
        instruction.processed_timestamp = time()
        self.processed_instructions.append(instruction)

        return instruction
