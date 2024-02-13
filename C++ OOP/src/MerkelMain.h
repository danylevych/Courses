#pragma once

#include <vector>
#include <string>
#include "OrderBook.h"

class MerkelMain
{
private:
    OrderBook orders;
    std::string currentTime;

public:
    MerkelMain();
    /** Call this to start the sim */
    void init();
private:
    void printMenu();

    void printHelp();
    void printMarketStats();
    void enterAsk();
    void enterBid();
    void printWallet();
    void gotoNextTimeframe();
    int getUserOption();
    void processUserOption(int userOption);
}; 
