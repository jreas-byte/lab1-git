#ifndef STORE_H
#define STORE_H

#include "Product.h"
#include <string>
#include <vector>
using namespace std;

class Store {
private:
    string name_;
    vector<Product> products_;

public:
    Store(const string &name);

    void addProduct(const Product &product);
    size_t count() const;
    double totalOrderValue() const;
    void printReport() const;
};

#endif
