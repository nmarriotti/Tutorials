#include <iostream>

using namespace std;

int main()
{
    int var = 100;
    int *ptr = &var;

    cout << ptr << endl;
    cout << *ptr << endl;

    return 0;
}
