from src.Market import Market
from src.Order import Order, OrderType, Side

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

    # Add these orders to the instruction queue as NEW_ORDER
    spy_market.instruction_queue.add_instruction(order1.to_new_order_instruction())




if __name__ == "__main__":
    main()