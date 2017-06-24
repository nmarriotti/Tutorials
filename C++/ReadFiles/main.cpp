#include <iostream>
#include <cmath>
#include <fstream>
#include <cstdlib>
using namespace std;

int main()
{
    char filename[50];
    ifstream myFile;
    cin.getline(filename, 50);
    myFile.open(filename);

    if(!myFile.is_open()) {
        exit(EXIT_FAILURE);
    }

    char word[50];
    myFile >> word;
    while(myFile.good()) {
        cout << word << " ";
        myFile >> word;
    }


    system("pause");
    return 0;
}
