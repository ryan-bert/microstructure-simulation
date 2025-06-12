#pragma once

#include <vector>
#include <string>
#include "Order.h"

class OrderBook {
public:
    OrderBook(const std::string& ticker);

    void addOrder(const Order& order);
    void removeOrder(int orderId);
    void printOrders() const;

    std::string getTicker() const;

private:
    std::string ticker;
    std::vector<Order> buyOrders;
    std::vector<Order> sellOrders;
};