#include <iostream>

using namespace std;

/* create macro function */
#define SQUARE(x) ((x) * (x))

int main()
{
    cout << SQUARE(10) << endl;
    return 0;
}
