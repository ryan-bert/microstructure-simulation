import time
import random
from src.Order import Order, Side, OrderType
from src.OrderBook import OrderBook

def main():

    print("Benchmarking add_order() performance...\n")
    
    sizes = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000]
    
    for num_orders in sizes:
        order_book = OrderBook()
        start_time = time.perf_counter()

        for i in range(num_orders):
            order = Order(
                order_id=i,
                side=random.choice([Side.BUY, Side.SELL]),
                quantity=random.randint(1, 100),
                order_type=OrderType.LIMIT,
                price=random.randint(90, 110)  # Simulate tight spread
            )
            order_book.add_order(order)

        end_time = time.perf_counter()
        elapsed = end_time - start_time
        print(f"Added {num_orders:>7,} orders in {elapsed:.10f} seconds")

if __name__ == "__main__":
    main()