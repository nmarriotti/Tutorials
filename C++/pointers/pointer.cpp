#include <iostream>
using namespace std;

void change(int&);
int main() {

    int* ptr;
    int x = 5;

    ptr = &x;

    //pass by reference
    change(*ptr);

    cout << ptr << endl;
    cout << *ptr << endl;

    return 0;
}

// value of pointer is changed out of scope
void change(int& num) {
    num = 10;
}