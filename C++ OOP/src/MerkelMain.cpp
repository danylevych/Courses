#include "MerkelMain.h"
#include <iostream>
#include <vector>
#include "OrderBookEntry.h"
#include "CSVReader.h"
#include <limits>

MerkelMain::MerkelMain()
    : orders("20200317.csv")
{   }

void MerkelMain::init()
{
    currentTime = orders.getEarliestTime();
    int input;
    while(true)
    {
        printMenu();
        input = getUserOption();
        processUserOption(input);
    }
}

void MerkelMain::printMenu()
{
    std::cout << "---------======== Main Menu ========---------" << std::endl;
    // 1 print help
    std::cout << "1: Print help " << std::endl;
    // 2 print exchange stats
    std::cout << "2: Print exchange stats" << std::endl;
    // 3 make an offer
    std::cout << "3: Make an ask " << std::endl;
    // 4 make a bid 
    std::cout << "4: Make a bid " << std::endl;
    // 5 print wallet
    std::cout << "5: Print wallet " << std::endl;
    // 6 continue   
    std::cout << "6: Continue " << std::endl;

    std::cout << "========================================" << std::endl;
    std::cout << "Current time: " << currentTime << std::endl;
    std::cout << "========================================" << std::endl;
}

void MerkelMain::printHelp()
{
    std::cout << "Help - your aim is to make money. Analyse the market and make bids and offers. " << std::endl;
}

void MerkelMain::printMarketStats()
{
    std::cout << "=========================== ASK ===========================" << std::endl;
    for (const auto& product : orders.getKnownBook())
    {
        std::cout << "Product: " << product << std::endl;

        auto entries = orders.getOrders(OrderBookType::ask, product, currentTime);
        std::cout << "         Ask seen: " << entries.size() << std::endl;
        std::cout << "         Max ask:  " << OrderBook::getHighPrice(entries) << std::endl;
        std::cout << "         Min ask:  " << OrderBook::getLowPrice(entries) << std::endl;

        std::string prevTime = orders.getPrevTime(currentTime);
        auto change = OrderBook::getChange(orders.getOrders(OrderBookType::ask, product, prevTime), entries);
        std::cout << "         Change:   " << change.first << "$ " << change.second / 100 * 100 << "%" << std::endl;
        std::cout << "---------------------------------------------------------------\n";
    }
    std::cout << "===========================================================" << std::endl;

    std::cout << "=========================== BID ===========================" << std::endl;
    for (const auto& product : orders.getKnownBook())
    {
        std::cout << "Product: " << product << std::endl;

        auto entries = orders.getOrders(OrderBookType::bid, product, currentTime);
        std::cout << "         Ask seen: " << entries.size() << std::endl;
        std::cout << "         Max bid:  " << OrderBook::getHighPrice(entries) << std::endl;
        std::cout << "         Min bid:  " << OrderBook::getLowPrice(entries) << std::endl;

        std::string prevTime = orders.getPrevTime(currentTime);
        auto change = OrderBook::getChange(orders.getOrders(OrderBookType::bid, product, prevTime), entries);
        std::cout << "         Change:   " << change.first << "$ " << change.second / 100 * 100 << "%" << std::endl;
        std::cout << "---------------------------------------------------------------\n";
    }
    std::cout << "===========================================================" << std::endl;


    system("pause");
}

void MerkelMain::enterAsk()
{
    std::cout << "Make an ask - enter the amount: (name,price,amount : eg. DOGE/USDT,200,0.5) " << std::endl;
    std::string askLine;

    // Ignore previous user input.
    // std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

    std::getline(std::cin, askLine);

    std::vector<std::string> tokens = CSVReader::tokenise(askLine, ',');

    if (tokens.size() != 3)
    {
        std::cout << "You entered bad format of ask string!" << std::endl;
    }
    else
    {
        try 
        {
            OrderBookEntry obj = CSVReader::stringsToOBE(tokens[1], tokens[2], currentTime, tokens[0], OrderBookType::ask);
            orders.insertOrder(obj);
        }
        catch (...)
        {
            std::cout << "Bad input in MerkelMain::enterAsk" << std::endl;
        }
    }
}

void MerkelMain::enterBid()
{
    std::cout << "Make a bid - enter the amount  (name,price,amount : eg. DOGE/USDT,200,0.5)" << std::endl;

    std::string lineInput;

    std::getline(std::cin, lineInput);

    std::vector<std::string> tokens = CSVReader::tokenise(lineInput, ',');

    if (tokens.size() != 3)
    {
        std::cout << "You entered bad format of bid string!" << std::endl;
    }
    else
    {
        try 
        {
            OrderBookEntry obj = CSVReader::stringsToOBE(tokens[1], tokens[2], currentTime, tokens[0], OrderBookType::bid);
            orders.insertOrder(obj);
        }
        catch (...)
        {
            std::cout << "Bad input in MerkelMain::enterBid" << std::endl;
        }
    }
}

void MerkelMain::printWallet()
{
    std::cout << "Your wallet is empty. " << std::endl;
}
        
void MerkelMain::gotoNextTimeframe()
{
    std::cout << "Going to next time frame. " << std::endl;
    currentTime = orders.getNextTime(currentTime);
}

int MerkelMain::getUserOption()
{
    int userOption = 0;
    std::string lineInput;

    std::cout << "Type in 1-6" << std::endl;

    std::getline(std::cin, lineInput);

    try
    {
        userOption = std::stoi(lineInput);
    }
    catch(...)
    {
        // We do not need to handle the exception that ocurred here, it will be bad input.
    }
    
    std::cout << "You chose: " << userOption << std::endl;
    return userOption;
}

void MerkelMain::processUserOption(int userOption)
{
    system("cls"); // Clear input.

    if (userOption == 0) // bad input
    {
        std::cout << "Invalid choice. Choose 1-6" << std::endl;
    }
    if (userOption == 1) 
    {
        printHelp();
    }
    if (userOption == 2) 
    {
        printMarketStats();
    }
    if (userOption == 3) 
    {
        enterAsk();
    }
    if (userOption == 4) 
    {
        enterBid();
    }
    if (userOption == 5) 
    {
        printWallet();
    }
    if (userOption == 6) 
    {
        gotoNextTimeframe();
    }
    
    system("pause"); // Wait till user press any key.
}
