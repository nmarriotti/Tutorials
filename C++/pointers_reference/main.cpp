#include <iostream>

using namespace std;


int main()
{

    // Create a pointer of type int
    int* myPointer = new int;

    cout << "How old are you? ";
    // Store value in myPointer
    cin >> *myPointer;

    // Get memory address of myPointer
    cout << "Age " << *myPointer << " is stored at " << myPointer << endl;

    // Change the value of myPointer
    *myPointer = 15;
    cout << "Changed value stored at " << myPointer << " to " << *myPointer << endl;


    delete myPointer;






    return 0;
}


