#include "OrderBook.h"
#include <iostream>
#include <algorithm>

OrderBook::OrderBook(const std::string& ticker) : ticker(ticker) {}

void OrderBook::addOrder(const Order& order) {
    if (order.getSide() == Side::Buy) {
        buyOrders.push_back(order);
    } else {
        sellOrders.push_back(order);
    }
}

void OrderBook::removeOrder(int orderId) {
    auto orderMatches = [orderId](const Order& order) {
        return order.getId() == orderId;
    };

    auto buyIterator = std::remove_if(buyOrders.begin(), buyOrders.end(), orderMatches);
    if (buyIterator != buyOrders.end()) {
        buyOrders.erase(buyIterator, buyOrders.end());
        return;
    }

    auto sellIterator = std::remove_if(sellOrders.begin(), sellOrders.end(), orderMatches);
    if (sellIterator != sellOrders.end()) {
        sellOrders.erase(sellIterator, sellOrders.end());
        return;
    }

    std::cout << "Order ID " << orderId << " not found in book.\n";
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