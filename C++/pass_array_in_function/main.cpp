#include <iostream>
#include <string>

using namespace std;

void print_array(string names[], int length) {
    for(int i=0; i<length; i++) {
        cout << names[i] << endl;
    }
}

int main()
{
    string x[] = {"Nick", "Stephanie", "Eli", "Alaina"};
    int length = sizeof(x)/sizeof(x[0]);
    print_array(x, length);

    return 0;
}
