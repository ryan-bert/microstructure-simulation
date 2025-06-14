from OrderBook import OrderBook
from Order import Order, OrderType, Side
from InstructionQueue import Instruction, InstructionType, InstructionQueue
from ExecutedTrades import Trade, ExecutedTrades
from MatchingEngine import MatchingEngine

class Market:

    # Constructor for the Market class
    def __init__(self):
        self.order_book = OrderBook()
        self.instruction_queue = InstructionQueue()
        self.executed_trades = ExecutedTrades()
        self.matching_engine = MatchingEngine(self.order_book, self.instruction_queue, self.executed_trades)