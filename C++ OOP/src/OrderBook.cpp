#include "OrderBook.h"

#include "CSVReader.h"
#include <map>
#include <set>
#include <algorithm>


OrderBook::OrderBook(const std::string &fileName)
{
    orders = CSVReader::readCSV(fileName);
}

std::vector<std::string> OrderBook::getKnownBook()
{
    std::set<std::string> productsSet;

    // Add unique products to the set.
    std::for_each(orders.begin(), orders.end(), [&productsSet](OrderBookEntry& entry) {
        productsSet.insert(entry.product);
    });

    // Create the vector of unique products.
    return std::vector<std::string>(productsSet.begin(), productsSet.end());
}

std::vector<OrderBookEntry> OrderBook::getOrders(OrderBookType type, std::string product, std::string timeStamp)
{
    std::vector<OrderBookEntry> ordersRes;

    // Find all maches element and push it into the vector.
    std::for_each(orders.begin(), orders.end(), [&ordersRes, &type, &product, &timeStamp](const OrderBookEntry& item) {
        if (item.orderType == type && item.product == product && item.timestamp == timeStamp)
        {
            ordersRes.push_back(item);
        }
    });

    return ordersRes;
}

std::string OrderBook::getEarliestTime() const
{
    return orders.at(0).timestamp;
}

std::string OrderBook::getNextTime(const std::string &timestamp) const
{
    std::string newTimestamp;

    // Find next timestamp.
    for (auto& item : orders)
    {
        if (item.timestamp > timestamp)
        {
            newTimestamp = item.timestamp;
            break;
        }
    }
    
    // If the stamp is not found wrap it back around the first item.
    if (newTimestamp.empty())
    {
        newTimestamp = orders.at(0).timestamp;
    }

    return newTimestamp;
}

std::string OrderBook::getPrevTime(const std::string &timestamp) const
{
    std::string newTimestamp = orders[0].timestamp;

    // Find prev timestamp.
    for (auto& item : orders)
    {
        if (item.timestamp < timestamp)
        {
            newTimestamp = item.timestamp;
            break;
        }
    }

    return newTimestamp;
}

void OrderBook::insertOrder(OrderBookEntry &order)
{
    orders.push_back(order);
    std::sort(orders.begin(), orders.end());
}

double OrderBook::getHighPrice(const std::vector<OrderBookEntry> &orders)
{
    // Find the highest price.
    return std::max_element(orders.begin(), orders.end(), [](const OrderBookEntry& left, const OrderBookEntry& right) {
        return left.price < right.price;
    })->price;
}

double OrderBook::getLowPrice(const std::vector<OrderBookEntry> &orders)
{
    // Find the lowest price.
    return std::min_element(orders.begin(), orders.end(), [](const OrderBookEntry& left, const OrderBookEntry& right) {
        return left.price < right.price;
    })->price;
}

std::pair<price, percent> OrderBook::getChange(const std::vector<OrderBookEntry>& prevOrders, const std::vector<OrderBookEntry> &orders)
{
    double basePrice = getHighPrice(prevOrders);
    double currentPrice = getHighPrice(orders);

    price diffPrice = basePrice - currentPrice;

    return std::pair<price, percent>(diffPrice, diffPrice / 100);
}
