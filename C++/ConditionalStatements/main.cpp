#include <iostream>

using namespace std;

int main()
{
    int x = 10;
    bool y = false;

    if(x == 10) {
        cout << "x is 10" << endl;
    }

    if(x <= 20) {
        cout << "x is LESS THAN OR EQUAL TO 20" << endl;
    }

    if(x >= 11) {
        cout << "x is GREATER THAN OR EQUAL TO 11" << endl;
    }

    if(x != 9) {
        cout << "x is NOT EQUAL to 9" << endl;
    }

    if(!y) {
        cout << "y is FALSE" << endl;
    }

    if(x == 1 || x == 10) {
        cout << "x is EQUAL to 10" << endl;
    }

    if(x < 20 && x > 0) {
        cout << "x is LESS THAN 20 and x is GREATER THAN 0" << endl;
    }

    return 0;
}
