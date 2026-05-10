#include "Product.h"
#include "Store.h"
#include <iostream>
using namespace std;

int main() {
    Store store("TechStore UA");

    store.addProduct(Product("Ноутбук", 25000.0, 1));
    store.addProduct(Product("Мишка", 500.0, 2));
    store.addProduct(Product("Клавіатура", 1200.0, 1));
    store.addProduct(Product("Монітор", 7000.0, 1));

    store.printReport();

    cout << "\nПеревірка: усього товарів = " << store.count() << endl;

    return 0;
}
