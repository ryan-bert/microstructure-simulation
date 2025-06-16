import time
import random
from src.Order import Order, OrderType, Side
from src.InstructionQueue import InstructionType
from src.Market import Market

NUM_LIMITS = 10000000
NUM_MARKETS = 10000000
TICKER = "SPEED"
MIN_QTY = 1
MAX_QTY = 20


def generate_limit_orders():
    orders = []
    quantities = []

    # Generate 1M random (non-marketable) buy limit orders
    for i in range(NUM_LIMITS // 2):
        price = 1000 - i * 0.001
        qty = random.randint(MIN_QTY, MAX_QTY)
        quantities.append(qty)
        orders.append(Order(order_id=i, side=Side.BUY, quantity=qty, order_type=OrderType.LIMIT, price=price))

    # Generate 1M random (non-marketable) sell limit orders
    for i in range(NUM_LIMITS // 2, NUM_LIMITS):
        price = 1000 + (i - NUM_LIMITS // 2) * 0.001
        qty = random.randint(MIN_QTY, MAX_QTY)
        quantities.append(qty)
        orders.append(Order(order_id=i, side=Side.SELL, quantity=qty, order_type=OrderType.LIMIT, price=price))

    return orders, quantities


def generate_market_orders(quantities):
    orders = []
    assert len(quantities) == NUM_MARKETS

    # Shuffle quantities for market orders
    shuffled_quantities = quantities[:]
    random.shuffle(shuffled_quantities)

    # Generate 1M market orders (half buy, half sell)
    for i in range(NUM_MARKETS // 2):
        orders.append(Order(order_id=NUM_LIMITS + i, side=Side.SELL, quantity=shuffled_quantities[i], order_type=OrderType.MARKET))
    for i in range(NUM_MARKETS // 2, NUM_MARKETS):
        orders.append(Order(order_id=NUM_LIMITS + i, side=Side.BUY, quantity=shuffled_quantities[i], order_type=OrderType.MARKET))

    return orders


def main():
    market = Market(TICKER)

    # Generate orders
    limit_orders, limit_quantities = generate_limit_orders()
    market_orders = generate_market_orders(limit_quantities)

    # Test 1: Add all limit orders
    t1_start = time.perf_counter()
    for order in limit_orders:
        market.order_book.add_order(order)
    t1_end = time.perf_counter()
    print(f"Test 1: Add 10M limit orders → {t1_end - t1_start:.2f} seconds")

    # Test 2: Remove all limit orders
    t2_start = time.perf_counter()
    for order in limit_orders:
        market.order_book.remove_order(order.id)
    t2_end = time.perf_counter()
    print(f"Test 2: Remove 10M limit orders → {t2_end - t2_start:.2f} seconds")

    # Test 3: Add 2M instructions
    t3_start = time.perf_counter()
    for order in limit_orders:
        market.instruction_queue.add_instruction(order.to_instruction(InstructionType.NEW_ORDER))
    for order in market_orders:
        market.instruction_queue.add_instruction(order.to_instruction(InstructionType.NEW_ORDER))
    t3_end = time.perf_counter()
    print(f"Test 3: Enqueue 20M instructions → {t3_end - t3_start:.2f} seconds")

    # Test 4: Process 1M limit orders
    t4_start = time.perf_counter()
    for _ in range(NUM_LIMITS):
        market.matching_engine.process_next_instruction()
    t4_end = time.perf_counter()
    print(f"Test 4: Process 10M limit instructions → {t4_end - t4_start:.2f} seconds")

    # Test 5: Process 1M market orders
    t5_start = time.perf_counter()
    for _ in range(NUM_MARKETS):
        market.matching_engine.process_next_instruction()
    t5_end = time.perf_counter()
    print(f"Test 5: Process 10M market orders → {t5_end - t5_start:.2f} seconds")

if __name__ == "__main__":
    main()