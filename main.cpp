#include <iostream>
#include "Order.h"
#include "OrderBook.h"

int main() {

    Order order1(1, Side::Buy, 100.50, 10, OrderType::Limit);
    Order order2(2, Side::Sell, 101.00, 5, OrderType::Market);
    Order order3(3, Side::Buy, 99.75, 20, OrderType::Limit);
    Order order4(4, Side::Sell, 102.25, 15, OrderType::Market);
    Order order5(5, Side::Buy, 98.00, 30, OrderType::Limit);
    Order order6(6, Side::Sell, 103.50, 25, OrderType::Market);
    Order order7(7, Side::Buy, 97.25, 40, OrderType::Limit);
    Order order8(8, Side::Sell, 104.75, 35, OrderType::Market);
    Order order9(9, Side::Buy, 96.50, 50, OrderType::Limit);
    Order order10(10, Side::Sell, 105.00, 45, OrderType::Market);

    OrderBook orderBook("AAPL");
    orderBook.addOrder(order1);
    orderBook.addOrder(order2);
    orderBook.addOrder(order3);
    orderBook.addOrder(order4);
    orderBook.addOrder(order5);
    orderBook.addOrder(order6);
    orderBook.addOrder(order7);
    orderBook.addOrder(order8);
    orderBook.addOrder(order9);
    orderBook.addOrder(order10);
    orderBook.printOrders();

    Order* pOrder1 = &order1;
    std::cout << pOrder1;

    return 0;
}