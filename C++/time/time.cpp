#include <iostream>
#include <ctime>
using namespace std;

int main() {

	time_t now = time(0);

	tm *localTime = localtime(&now);

	cout << "Year " << 1900 + localTime->tm_year << endl;
	cout << "Month " << 1 + localTime->tm_mon << endl;
	cout << "Day " << localTime->tm_mday << endl;
	cout << "Time: " << localTime->tm_hour << ":" << localTime->tm_min << ":" << localTime->tm_sec << endl;
	

	return 0;
}
