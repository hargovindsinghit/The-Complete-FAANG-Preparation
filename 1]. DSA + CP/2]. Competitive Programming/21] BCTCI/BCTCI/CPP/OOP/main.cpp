// Simplified OOP Stock Market System in C++
#include <iostream>
#include <vector>

using namespace std;

// Base class: Stock
class Stock {
protected:
    string symbol;
    double price;

public:
    Stock(const string& sym, double p) : symbol(sym), price(p) {}
    virtual void display() const {
        cout << "Stock: " << symbol << " | Price: " << price << endl;
    }
};

// Derived class: TechStock
class TechStock : public Stock {
public:
    TechStock(const string& sym, double p) : Stock(sym, p) {}
    void display() const override {
        cout << "[Tech] " << symbol << " | Price: " << price << endl;
    }
};

// Trader class
class Trader {
private:
    string name;
    double balance;
    vector<Stock*> portfolio;

public:
    Trader(const string& n, double b) : name(n), balance(b) {}
    
    void buyStock(Stock* stock) {
        if (balance >= stock->display()) {
            balance -= stock->display();
            portfolio.push_back(stock);
            cout << name << " bought " << stock->display() << endl;
        } else {
            cout << "Insufficient balance!" << endl;
        }
    }

    void displayPortfolio() const {
        cout << "Portfolio of " << name << ":\n";
        for (const auto& stock : portfolio) {
            stock->display();
        }
        cout << "Balance: " << balance << endl;
    }
};

int main() {
    TechStock apple("AAPL", 150.0);
    TechStock google("GOOG", 2800.0);

    Trader trader("John Doe", 5000);
    trader.buyStock(&apple);
    trader.buyStock(&google);
    trader.displayPortfolio();

    return 0;
}
