#include "OrderBook.h"
#include <iostream>

OrderBook::OrderBook(const std::string& ticker) : ticker(ticker) {}

void OrderBook::addOrder(const Order& order) {
    if (order.getSide() == Side::Buy) {
        buyOrders.push_back(order);
    } else {
        sellOrders.push_back(order);
    }
}

void OrderBook::printOrders() const {
    std::cout << "Order Book for " << ticker << std::endl;

    std::cout << "Buy Orders:\n";
    for (const auto& order : buyOrders) {
        std::cout << "  ID: " << order.getId()
                  << ", Price: " << order.getPrice()
                  << ", Qty: " << order.getQuantity() << "\n";
    }

    std::cout << "Sell Orders:\n";
    for (const auto& order : sellOrders) {
        std::cout << "  ID: " << order.getId()
                  << ", Price: " << order.getPrice()
                  << ", Qty: " << order.getQuantity() << "\n";
    }
}

std::string OrderBook::getTicker() const {
    return ticker;
}