#pragma once

// Define OrderType and Side enums
enum class OrderType { Market, Limit };
enum class Side { Buy, Sell };

class Order {

public:
    // Constructor
    Order(int id, Side side, double price, int quantity, OrderType type);

    // Getters
    int getId() const;
    Side getSide() const;
    double getPrice() const;
    int getQuantity() const;
    OrderType getType() const;

private:
    // Member variables
    int id;
    Side side;
    double price;
    int quantity;
    OrderType type;
};