#include <iostream>
#include <string>
using namespace std;

int main()
{
    string str = "Today is going to be a great day!";
    string sub = "going";
    size_t charPos = str.find(sub, 0);

    if (charPos != string::npos) {
        cout << "First instance of '" << sub << "' was found at position " << charPos << endl;
    } else {
        cout << "String not found" << endl;
    }

    return 0;
}
