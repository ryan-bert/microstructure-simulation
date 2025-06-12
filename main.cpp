#include <iostream>
#include "Order.h"

int main() {

    Order order(1, Side::Buy, 100.50, 10, OrderType::Limit);
    std::cout << "Order ID: " << order.getId() << std::endl;

    return 0;
}