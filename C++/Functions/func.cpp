#include <iostream>
using namespace std;


void myFunction();
int add(int, int);

int main() {

    int num1, num2;

    myFunction();

    cout << "Enter a number: ";
    cin >> num1;
    cout << "Enter another number: ";
    cin >> num2;

    cout << add(num1, num2) << endl;

    return 0;
}


void myFunction() {
    cout << "This is the function." << endl;
}


int add(int x, int y) {
    int answer = x + y;
    return answer;
}


