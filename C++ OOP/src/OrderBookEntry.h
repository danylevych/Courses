#pragma once

#include <string>

enum class OrderBookType { bid, ask, unknown };

class OrderBookEntry
{
public:
    double price;
    double amount;
    std::string timestamp;
    std::string product;
    OrderBookType orderType;

public:
    OrderBookEntry( double _price, 
                    double _amount, 
                    std::string _timestamp, 
                    std::string _product, 
                    OrderBookType _orderType);

public:
    bool operator<(const OrderBookEntry& right) const;

public:
    static OrderBookType stringToOrderBookType(std::string s);
};
