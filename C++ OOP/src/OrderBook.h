#pragma once

#include "OrderBookEntry.h"
#include <vector>
#include <string>
#include <utility>

using price = double;
using percent = double;

class OrderBook
{
private:
    std::vector<OrderBookEntry> orders;

public:
    OrderBook(const std::string& fileName);

public:
    /**
     *  Return the vector of unique products.
    */
    std::vector<std::string> getKnownBook();

    /**
     *  Return all products which corecponding the condistion.
    */
    std::vector<OrderBookEntry> getOrders(OrderBookType type, std::string product, std::string timeStamp);

    /**
     *  Return the elierst timestamp.
    */
    std::string getEarliestTime() const;

    /**
     *  Return the next timestamp after given.
     *  If the the time stamp come to the end wraps it to the first element.
    */
    std::string getNextTime(const std::string& timestamp) const;

    /**
     *  Return the previous timestamp if it posible, otherwise - return the first time stamp for orders.
    */
    std::string getPrevTime(const std::string &timestamp) const;

    /**
     *  Insert value into container.
    */
    void insertOrder(OrderBookEntry& order);
    
public:
    /**
     *  Return the highest price of the product.
    */
    static double getHighPrice(const std::vector<OrderBookEntry>& orders);

    /**
     *  Return the lowest price of the product.
    */
    static double getLowPrice(const std::vector<OrderBookEntry>& orders);

    /**
     *  Return the change between base and curent prices.
    */
    static std::pair<price, percent> getChange(const std::vector<OrderBookEntry>& prevOrders, const std::vector<OrderBookEntry>& orders);
};