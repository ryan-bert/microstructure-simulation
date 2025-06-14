#include "OrderBook.h"
#include <iostream>
#include <algorithm>

// Constructor for OrderBook class
OrderBook::OrderBook(const std::string& ticker) : ticker(ticker) {}

// Method to add an order to the order book
void OrderBook::addOrder(const Order& order) {

    // Add order to the END of respective vector
    if (order.getSide() == Side::Buy) {
        buyOrders.push_back(order);
    } else {
        sellOrders.push_back(order);
    }
}

// Method to remove an order from the order book (by order ID)
void OrderBook::removeOrder(int orderId){

    // Lambda function to match an order by ID
    auto orderMatches = [orderId](const Order& order) {
        return order.getId() == orderId;
    };

    // Re-order dead buys to last (and return iterator to the first dead buy)
    auto startOfDeadBuys = std::remove_if(buyOrders.begin(), buyOrders.end(), orderMatches);
    // If dead buys are found, resize the vector to remove them
    if (startOfDeadBuys != buyOrders.end()) {
        buyOrders.erase(startOfDeadBuys, buyOrders.end());
        return;
    }

    // Re-order dead sells to last (and return iterator to the first dead sell)
    auto sellIterator = std::remove_if(sellOrders.begin(), sellOrders.end(), orderMatches);
    // If dead sells are found, resize the vector to remove them
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