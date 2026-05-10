#include "Product.h"

Product::Product(const string &name, double price, int quantity)
    : name_(name), price_(price), quantity_(quantity) {}

const string &Product::name() const {
    return name_;
}

double Product::price() const {
    return price_;
}

int Product::quantity() const {
    return quantity_;
}

double Product::totalPrice() const {
    return price_ * quantity_;
}
