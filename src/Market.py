from src.OrderBook import OrderBook
from src.InstructionQueue import InstructionQueue
from src.ExecutedTrades import ExecutedTrades
from src.MatchingEngine import MatchingEngine

class Market:

    # Constructor for the Market class
    def __init__(self, ticker):
        self.ticker = ticker
        self.order_book = OrderBook()
        self.instruction_queue = InstructionQueue()
        self.executed_trades = ExecutedTrades()
        self.matching_engine = MatchingEngine(self.order_book, self.instruction_queue, self.executed_trades)