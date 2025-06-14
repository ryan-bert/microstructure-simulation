from src.Order import Order, OrderType, Side
from src.OrderBook import OrderBook

def main():

    # Create an orderboom for a given ticker
    spy_order_book = OrderBook("SPY")

    # Create some liquidity
    order1 = Order(order_id=1, side=Side.BUY, price=100.0, quantity=10, order_type=OrderType.LIMIT)
    order2 = Order(order_id=2, side=Side.SELL, price=100.0, quantity=5, order_type=OrderType.LIMIT)
    order3 = Order(order_id=3, side=Side.BUY, price=100.0, quantity=15, order_type=OrderType.LIMIT)
    order4 = Order(order_id=4, side=Side.SELL, price=102.0, quantity=20, order_type=OrderType.LIMIT)
    order5 = Order(order_id=5, side=Side.BUY, price=98.0, quantity=8, order_type=OrderType.LIMIT)
    order6 = Order(order_id=6, side=Side.SELL, price=103.0, quantity=12, order_type=OrderType.LIMIT)
    order7 = Order(order_id=7, side=Side.BUY, price=97.0, quantity=6, order_type=OrderType.LIMIT)
    order8 = Order(order_id=8, side=Side.SELL, price=104.0, quantity=10, order_type=OrderType.LIMIT)
    order9 = Order(order_id=9, side=Side.BUY, price=104.0, quantity=4, order_type=OrderType.LIMIT)

    # Add orders to the order book
    spy_order_book.add_order(order1)
    spy_order_book.add_order(order2)
    spy_order_book.add_order(order3)
    spy_order_book.add_order(order4)
    spy_order_book.add_order(order5)
    spy_order_book.add_order(order6)
    spy_order_book.add_order(order7)
    spy_order_book.add_order(order8)
    spy_order_book.add_order(order9)

    # Remove an order
    spy_order_book.remove_order(order_id=3)

    # Print the order book
    print("Bids:")
    for price, orders in spy_order_book.bids.items():
        print(f"Price: {price}, Orders: {[order.id for order in orders]}")
    print("\nAsks:")
    for price, orders in spy_order_book.asks.items():
        print(f"Price: {price}, Orders: {[order.id for order in orders]}")


if __name__ == "__main__":
    main()