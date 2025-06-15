from src.Market import Market
from src.Order import Order, OrderType, Side
from src.InstructionQueue import InstructionType

#! TODO: BASIC SIMULATION
# - Instructions getting added to queue
# - MatchingEngine processing instructions
# - Live output
# - Stored summary files

def main():
    
    # Create market for SPY
    spy_market = Market("SPY")

    # Create some liquidity
    order1 = Order(order_id=1, side=Side.BUY, quantity=10, order_type=OrderType.LIMIT, price=101)
    order2 = Order(order_id=2, side=Side.BUY, quantity=15, order_type=OrderType.LIMIT, price=100)
    order3 = Order(order_id=3, side=Side.BUY, quantity=20, order_type=OrderType.LIMIT, price=99)
    order4 = Order(order_id=4, side=Side.SELL, quantity=10, order_type=OrderType.LIMIT, price=102)
    order5 = Order(order_id=5, side=Side.SELL, quantity=15, order_type=OrderType.LIMIT, price=103)
    order6 = Order(order_id=6, side=Side.SELL, quantity=20, order_type=OrderType.LIMIT, price=104)
    order7 = Order(order_id=7, side=Side.SELL, quantity=25, order_type=OrderType.LIMIT, price=102)
    order8 = Order(order_id=8, side=Side.SELL, quantity=30, order_type=OrderType.LIMIT, price=103)
    order9 = Order(order_id=9, side=Side.SELL, quantity=35, order_type=OrderType.LIMIT, price=104)
    order10 = Order(order_id=10, side=Side.BUY, quantity=40, order_type=OrderType.LIMIT, price=101)
    order11 = Order(order_id=11, side=Side.BUY, quantity=45, order_type=OrderType.LIMIT, price=100)
    order12 = Order(order_id=12, side=Side.BUY, quantity=50, order_type=OrderType.LIMIT, price=99)

    # Add market orders
    order1_market = Order(order_id=13, side=Side.SELL, quantity=45, order_type=OrderType.MARKET)

    # Add these orders to the instruction queue as NEW_ORDER
    spy_market.instruction_queue.add_instruction(order1.to_instruction(InstructionType.NEW_ORDER))
    spy_market.instruction_queue.add_instruction(order2.to_instruction(InstructionType.NEW_ORDER))
    spy_market.instruction_queue.add_instruction(order3.to_instruction(InstructionType.NEW_ORDER))
    spy_market.instruction_queue.add_instruction(order4.to_instruction(InstructionType.NEW_ORDER))
    spy_market.instruction_queue.add_instruction(order5.to_instruction(InstructionType.NEW_ORDER))
    spy_market.instruction_queue.add_instruction(order6.to_instruction(InstructionType.NEW_ORDER))
    spy_market.instruction_queue.add_instruction(order7.to_instruction(InstructionType.NEW_ORDER))
    spy_market.instruction_queue.add_instruction(order8.to_instruction(InstructionType.NEW_ORDER))
    spy_market.instruction_queue.add_instruction(order9.to_instruction(InstructionType.NEW_ORDER))
    spy_market.instruction_queue.add_instruction(order10.to_instruction(InstructionType.NEW_ORDER))
    spy_market.instruction_queue.add_instruction(order11.to_instruction(InstructionType.NEW_ORDER))
    spy_market.instruction_queue.add_instruction(order12.to_instruction(InstructionType.NEW_ORDER))
    spy_market.instruction_queue.add_instruction(order1_market.to_instruction(InstructionType.NEW_ORDER))

    # Process the instructions in the queue
    while not spy_market.instruction_queue.is_empty():
        spy_market.matching_engine.process_next_instruction()

    # Print the order book after processing
    spy_market.order_book.print_order_book()


if __name__ == "__main__":
    main()