#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ifstream myFile("file.csv");

    int id;
    string name;
    double freq;

    cout << "Hello" << endl;

    while(myFile.is_open()) {
        cout << id << "," << name << "," << freq << endl;
    }
    return 0;
}
