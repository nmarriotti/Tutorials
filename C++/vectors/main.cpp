#include <iostream>
#include <vector>

using namespace std;

int main()
{
    vector<string> myStrings(3);

    myStrings[0] = "Sally";
    myStrings[1] = "Jim";
    myStrings[2] = "Steve";

    cout << "Size of vector is " << myStrings.size() << endl;

    for(int i=0; i<myStrings.size(); i++) {
        cout << myStrings[i] << endl;
    }



    return 0;
}
