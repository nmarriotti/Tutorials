#include<iostream>
#include<unordered_set>
#include<string>
using namespace std;

int main() {

    unordered_set<string> values;  // create unordered_set object
    
    values.insert("Blue"); // insert value of 10
    values.insert("Orange");
    values.insert("Green");

    for(string x : values) {
        cout << x << endl;
    } 

    cout << "Size of unordered_set: " << values.size() << endl;

    for(string x : values) {
        if(values.find("Gray") != values.end())
            cout << "Found the color Blue!" << endl;
        else
            cout << "Sorry couldn't find the color Blue!" << endl;

        break;
    }

    return 0;
}