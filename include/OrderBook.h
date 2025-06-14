#pragma once

#include <vector>
#include <string>
#include "Order.h"

class OrderBook {

public:
    // Constructor
    OrderBook(const std::string& ticker);

    // Methods to manage orders
    void addOrder(const Order& order);
    void removeOrder(int orderId);
    void printOrders() const;

    // Getters
    std::string getTicker() const;

private:
    // Member variables
    std::string ticker;
    std::vector<Order> buyOrders;
    std::vector<Order> sellOrders;
};