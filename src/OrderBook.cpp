#include "OrderBook.h"
#include <iostream>
#include <algorithm>

// Constructor for OrderBook
OrderBook::OrderBook(const std::string& ticker) : ticker(ticker) {}

// Adds a new order to the appropriate map based on side
void OrderBook::addOrder(const Order& order) {
    auto* book = (order.getSide() == Side::Buy) ? &buyOrders : &sellOrders;
    (*book)[order.getPrice()].push_back(order);
}

// Attempts to remove an order by ID from a given order map (buy or sell)
// Returns true if the order was found and removed, false otherwise
bool OrderBook::removeOrderFromBook(std::map<double, std::deque<Order>>& book, int orderId) {
    for (auto it = book.begin(); it != book.end(); ) {
        auto& orders = it->second;

        // Remove the matching order(s) from the queue
        auto removeIt = std::remove_if(orders.begin(), orders.end(), [orderId](const Order& order) {
            return order.getId() == orderId;
        });

        if (removeIt != orders.end()) {
            orders.erase(removeIt, orders.end());

            // If no more orders at this price level, erase the level
            if (orders.empty()) {
                it = book.erase(it);
            } else {
                ++it;
            }
            return true;
        } else {
            ++it;
        }
    }
    return false;
}

// Removes an order by ID, trying both buy and sell maps
void OrderBook::removeOrder(int orderId) {
    if (removeOrderFromBook(buyOrders, orderId)) return;
    if (removeOrderFromBook(sellOrders, orderId)) return;

    std::cout << "Order ID " << orderId << " not found in book.\n";
}

// Prints the current state of the order book
void OrderBook::printOrders() const {
    std::cout << "Order Book for " << ticker << std::endl;

    std::cout << "Buy Orders (Highest to Lowest):\n";
    for (const auto& [price, orders] : buyOrders) {
        for (const auto& order : orders) {
            std::cout << "  ID: " << order.getId()
                      << ", Price: " << order.getPrice()
                      << ", Qty: " << order.getQuantity() << "\n";
        }
    }

    std::cout << "Sell Orders (Lowest to Highest):\n";
    for (const auto& [price, orders] : sellOrders) {
        for (const auto& order : orders) {
            std::cout << "  ID: " << order.getId()
                      << ", Price: " << order.getPrice()
                      << ", Qty: " << order.getQuantity() << "\n";
        }
    }
}

// Returns the ticker associated with this order book
std::string OrderBook::getTicker() const {
    return ticker;
}