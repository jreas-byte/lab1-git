#ifndef PRODUCT_H
#define PRODUCT_H

#include <string>
using namespace std;

class Product {
private:
    string name_;
    double price_;
    int quantity_;

public:
    Product(const string &name, double price, int quantity);

    const string &name() const;
    double price() const;
    int quantity() const;
    double totalPrice() const;
};

#endif
