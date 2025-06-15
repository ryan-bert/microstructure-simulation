import unittest
from src.Order import Order, OrderType, Side
from src.OrderBook import OrderBook

class TestOrderBook(unittest.TestCase):

    # Applied before each test case
    def setUp(self):

        # Initialise empty order book
        self.book = OrderBook()
        # Bids: willing to buy at 101, 100, 99
        self.book.add_order(Order(order_id=1, side=Side.BUY, quantity=10, order_type=OrderType.LIMIT, price=101))
        self.book.add_order(Order(order_id=2, side=Side.BUY, quantity=15, order_type=OrderType.LIMIT, price=100))
        self.book.add_order(Order(order_id=3, side=Side.BUY, quantity=20, order_type=OrderType.LIMIT, price=99))
        # Asks: willing to sell at 102, 103, 104
        self.book.add_order(Order(order_id=4, side=Side.SELL, quantity=10, order_type=OrderType.LIMIT, price=102))
        self.book.add_order(Order(order_id=5, side=Side.SELL, quantity=15, order_type=OrderType.LIMIT, price=103))
        self.book.add_order(Order(order_id=6, side=Side.SELL, quantity=20, order_type=OrderType.LIMIT, price=104))


    # Test adding an order
    def test_add_order(self):

        # Snapshot of original queue
        original_queue = list(self.book.bids[101])
        self.assertEqual(len(original_queue), 1)
        self.assertEqual(original_queue[0].id, 1)

        # Add new bid at same price level (101)
        new_order = Order(order_id=10, side=Side.BUY, quantity=5, order_type=OrderType.LIMIT, price=101)
        self.book.add_order(new_order)

        # Assert: Queue at 101 should have 2 orders, new one last
        updated_queue = self.book.bids[101]
        self.assertEqual(len(updated_queue), 2)
        self.assertEqual(updated_queue[-1].id, 10)

        # Assert: All other price levels and orders unchanged
        self.assertEqual(len(self.book.bids[100]), 1)
        self.assertEqual(self.book.bids[100][0].id, 2)
        self.assertEqual(len(self.book.bids[99]), 1)
        self.assertEqual(self.book.bids[99][0].id, 3)
        self.assertEqual(len(self.book.asks[102]), 1)
        self.assertEqual(self.book.asks[102][0].id, 4)
        self.assertEqual(len(self.book.asks[103]), 1)
        self.assertEqual(self.book.asks[103][0].id, 5)
        self.assertEqual(len(self.book.asks[104]), 1)
        self.assertEqual(self.book.asks[104][0].id, 6)


    # Test removing an order
    def test_remove_order(self):

        # Remove order with ID 2 at price level 100
        removed = self.book.remove_order(2)

        # Assert: Correct order returned
        self.assertIsNotNone(removed)
        self.assertEqual(removed.id, 2)

        # Assert: Order should be removed
        self.assertNotIn(2, [o.id for o in self.book.bids.get(100, [])])

        # Assert: Lookup should be updated
        self.assertNotIn(2, self.book.order_lookup)

        # Price level 100 should NOT exist (no orders)
        self.assertNotIn(100, self.book.bids)


    # Test updating an order's price
    def test_update_order_price(self):

        # Order 1 is originally at price 101
        self.assertIn(1, [o.id for o in self.book.bids[101]])

        # Update price to 98
        self.book.update_order_price(1, 98)

        # Assert: Order removed from old price level
        self.assertNotIn(1, [o.id for o in self.book.bids.get(101, [])])

        # Assert: Order now exists at new price level
        self.assertIn(98, self.book.bids)
        self.assertEqual(self.book.bids[98][-1].id, 1)

        # Assert: Lookup is updated
        self.assertEqual(self.book.order_lookup[1], (Side.BUY, 98))


if __name__ == '__main__':
    unittest.main()