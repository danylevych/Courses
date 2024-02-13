#pragma once

#include "OrderBookEntry.h"
#include <vector>
#include <string>

class CSVReader
{
public:
    CSVReader();

    static std::vector<OrderBookEntry> readCSV(std::string csvFile);
    static std::vector<std::string> tokenise(std::string csvLine, char separator);
    
    static OrderBookEntry stringsToOBE(const std::string& price, const std::string& amount, const std::string& timestamp,
                                        const std::string& product, OrderBookType type);

private:
    static OrderBookEntry stringsToOBE(std::vector<std::string> strings);

}; 
