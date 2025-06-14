from OrderBook import OrderBook
from Order import Order, OrderType, Side
from InstructionQueue import Instruction, InstructionType, InstructionQueue
from ExecutedTrades import Trade, ExecutedTrades

class MatchingEngine:

    # Constructor for the MatchingEngine class
    def __init__(self, order_book, instruction_queue, executed_trades):
        self.order_book = order_book
        self.instruction_queue = instruction_queue
        self.executed_trades = executed_trades

