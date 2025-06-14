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
        
        # Get the next instruction from the queue
        instruction = self.instruction_queue.process_next_instruction()

        # If no instruction is available, return
        if not instruction:
            return

        # Process new order instructions
        if instruction.type == InstructionType.NEW_ORDER:

            # Process new order instruction
            order = instruction.order

            # Process order based on its type
            if order.type == OrderType.MARKET:
                self.match_market_order(order)
            elif order.type == OrderType.LIMIT:
                self.place_limit_order(order)
            else:
                raise ValueError("Invalid order type")
            
        # Process cancel order instructions
        elif instruction.type == InstructionType.CANCEL_ORDER:
            self.order_book.remove_order(instruction.order.id)

        # Process price update instructions
        elif instruction.type == InstructionType.UPDATE_PRICE:
            self.order_book.update_order_price(instruction.order.id, instruction.order.price)

        # Process quantity update instructions
        elif instruction.type == InstructionType.UPDATE_QUANTITY:
            self.order_book.update_order_quantity(instruction.order.id, instruction.order.quantity)

        # Invalid instruction type
        else:
            raise ValueError("Invalid instruction type")


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

        # Determine book and price matching condition
        if order.side == Side.BUY:
            book = self.order_book.asks
            price_is_matchable = lambda p: p <= order.price
        else:
            book = self.order_book.bids
            price_is_matchable = lambda p: p >= order.price

        # Define order quantity to fill
        quantity_to_fill = order.quantity

        # Iterate through (if any) marketable price levels
        while quantity_to_fill > 0 and book:

            # Define best price level and its associated queue
            best_price = next(iter(book))
            queue = book[best_price]

            # Break if it is NOT an marketable limit order
            if not price_is_matchable(best_price):
                break

            # Iterate through marketable orders at the best price
            while queue and quantity_to_fill > 0:

                # Define the resting order and match quantity
                resting_order = queue[0]
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

                # Adjust quantities after trade
                quantity_to_fill -= match_qty
                resting_order.quantity -= match_qty

                # Remove resting order if filled
                if resting_order.quantity == 0:
                    queue.popleft()

            # Remove price level if empty
            if not queue:
                del book[best_price]

        # Place non-marketable portion of limit order on the book
        if quantity_to_fill > 0:

            # Create a copy of the order with remaining quantity
            remaining_order = Order(
                order_id=order.id,
                side=order.side,
                price=order.price,
                quantity=quantity_to_fill,
                order_type=order.type
            )
            self.order_book.add_order(remaining_order)