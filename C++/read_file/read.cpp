#include <iostream>
#include <fstream>
using namespace std;

int main() {
	ifstream myfile("test.txt");
	string line;

	if(myfile.open()) {
		while(line == myfile.getline()) {
			cout << line << endl;
		}
	}

}
