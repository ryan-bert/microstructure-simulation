#pragma once

enum class OrderType { Market, Limit };
enum class Side { Buy, Sell };

class Order {
public:
    Order(int id, Side side, double price, int quantity, OrderType type);

    int getId() const;
    Side getSide() const;
    double getPrice() const;
    int getQuantity() const;
    OrderType getType() const;

private:
    int id;
    Side side;
    double price;
    int quantity;
    OrderType type;
};