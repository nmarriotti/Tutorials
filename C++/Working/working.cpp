// working.cpp by Bill Weinman <http://bw.org/>
#include <iostream>
#include "GetAge.h"
using namespace std;


int main( int argc, char ** argv ) {

	int birthYear;

	cout << "What is your birth year? ";
	cin >> birthYear;

	cout << "You are " << GetAge(birthYear) << endl;
	return 0;
}
