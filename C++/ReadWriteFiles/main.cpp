#include <iostream>
#include <fstream>

using namespace std;

void writeFile();

int main()
{
    writeFile();
    return 0;
}

void writeFile() {

    ofstream myFile ("example.txt");

    if(myFile.is_open()) {
        myFile << "This is line one.\n";
        myFile << "This is line two.\n";
        myFile.close();
        cout << "File saved." << endl;
    } else {
        cout << "Unable to open file.";
    }
}
