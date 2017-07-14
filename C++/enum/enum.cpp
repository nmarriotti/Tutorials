#include <iostream>
using namespace std;

// enums hold integer values
enum Animals { dog, cat, hamster, horse, cow };
enum class Colors { red, green, brown, blue, orange };

int main() {
    cout << hamster << endl;
    cout << (int)Colors::blue << endl;
    return 0;
}