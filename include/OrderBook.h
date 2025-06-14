#pragma once

#include <map>
#include <deque>
#include <string>
#include "Order.h"

class OrderBook {

public:
    // Constructor
    OrderBook(const std::string& ticker);

    // Functions to manage orders
    void addOrder(const Order& order);
    void removeOrder(int orderId);
    void printOrders() const;

    // Getters
    std::string getTicker() const;

private:
    // Member variables
    std::string ticker;

    // Ordered maps for buy and sell orders (default: ascending)
    std::map<double, std::deque<Order>, std::greater<>> buyOrders;
    std::map<double, std::deque<Order>> sellOrders;

    // Helper functions
    bool removeOrderFromBook(std::map<double, std::deque<Order>>& book, int orderId);
};