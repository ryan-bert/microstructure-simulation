#include "Order.h"

// Constructor for Order class
Order::Order(int id, Side side, double price, int quantity, OrderType type)
    : id(id), side(side), price(price), quantity(quantity), type(type) {}

// Getter methods
int Order::getId() const { return id; }
Side Order::getSide() const { return side; }
double Order::getPrice() const { return price; }
int Order::getQuantity() const { return quantity; }
OrderType Order::getType() const { return type; }