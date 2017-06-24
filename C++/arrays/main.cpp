#include <iostream>
#include <vector>

using namespace std;

int main()
{

    // Static
    const int LENGTH = 5
    int myNumbers [LENGTH] = {1, 2, 3, 4, 5};
    cout << "Value at index 2 is " << myNumbers[2] << endl;


    // Dynamic
    vector<int> dynArray (5);

    // Set our 5 values
    dynArray[0] = 5;
    dynArray[1] = 7;
    dynArray[2] = 10;
    dynArray[3] = 35;
    dynArray[4] = 41;


    cout << "Size of dynArray is " << dynArray.size() << endl;

    // Add two more values
    dynArray.push_back(55);
    dynArray.push_back(100);


    cout << "Size of dynArray is " << dynArray.size() << endl;



    return 0;
}
