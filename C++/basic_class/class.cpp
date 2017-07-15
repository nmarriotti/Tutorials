#include <iostream>
using namespace std;

class ShoppingCart {
    private:
        int items;
        double balance;

    public:
        ShoppingCart() {
            cout << "This is the constructor\n";
            items = 0;
            balance = 0;
        }

        void update_item_quantity(int x) {
            items += x;
        }

        int get_item_count() {
            return items;
        }
};

int main() {
    ShoppingCart x;
    x.update_item_quantity(10);
    cout << "Item quantity: " << x.get_item_count() << endl;
}