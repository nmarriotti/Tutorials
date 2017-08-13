#include <iostream>
using namespace std;

int get_length(char*);

int main() {
	
	char name[] = {"Alaina"};
	char* ptr;	
	ptr = name;
	
	// Print length of array
	cout << "Array length: " << get_length(ptr) << endl;

	return 0;
}

// Function to get length of array
int get_length(char* x) {
	return sizeof(x)/sizeof(x[0])-1;
}
