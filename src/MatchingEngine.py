from OrderBook import OrderBook
from Order import Order, OrderType, Side
from InstructionQueue import Instruction, InstructionType, InstructionQueue
from ExecutedTrades import Trade, ExecutedTrades
from time import time

class MatchingEngine:

    # Constructor for the MatchingEngine class
    def __init__(self, order_book, instruction_queue, executed_trades):
        self.order_book = order_book
        self.instruction_queue = instruction_queue
        self.executed_trades = executed_trades
        self.trade_id_counter = 1


    # Method to process the next instruction in the queue
    def process_next_instruction(self):
        return


    # Method to match market orders
    def match_market_order(self, order):

        # Determine the opposite book
        if order.side == Side.BUY:
            book = self.order_book.asks
        elif order.side == Side.SELL:
            book = self.order_book.bids
        else:
            raise ValueError("Invalid order side")

        # Check for NO liquidity, if so, cancel the order (ie do nothing)
        if not book:
            return

        # Define quantity to fill (for iteration)
        quantity_to_fill = order.quantity

        # Iterate through the book to fill the order
        while quantity_to_fill > 0 and book:

            # Get the best price level and its associated queue
            best_price = next(iter(book))
            order_queue = book[best_price]

            # Iterate over orders at current best price
            while order_queue and quantity_to_fill > 0:

                # Get the resting order at the best price
                resting_order = order_queue[0]
                match_qty = min(quantity_to_fill, resting_order.quantity)

                # Create a Trade object
                trade = Trade(
                    trade_id=self.trade_id_counter,
                    buy_order_id=order.id if order.side == Side.BUY else resting_order.id,
                    sell_order_id=order.id if order.side == Side.SELL else resting_order.id,
                    price=best_price,
                    quantity=match_qty,
                    timestamp=time()
                )

                # Log the trade and increment counter
                self.executed_trades.log_trade(trade)
                self.trade_id_counter += 1

                # Adjust quantities
                quantity_to_fill -= match_qty
                resting_order.quantity -= match_qty

                # Remove resting order if filled
                if resting_order.quantity == 0:
                    order_queue.popleft()

            # Remove empty price level
            if not order_queue:
                del book[best_price]


    # Method to place limit orders
    def place_limit_order(self, order):
        