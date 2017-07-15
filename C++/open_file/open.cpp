#include <iostream>
#include <fstream>
#include <string>
#include <stdio.h>
using namespace std;

int main() {
    ifstream FILE;
    string line;
    char filename[256];

    printf("File to open: ");
    cin.getline(filename, 256);

    FILE.open(filename);

    if(FILE.is_open()) {
        printf("File opened successfully!\n");
        while(getline(FILE, line)) {
            cout << line.length() << endl;
        }
    } else {
        printf("Unable to open file.");
    }

    return 0;
}