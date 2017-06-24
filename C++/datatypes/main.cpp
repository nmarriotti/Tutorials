#include <iostream>
#include <math.h>

using namespace std;

int main()
{
    int age = 10;
    float money = 50.25;
    double pi = M_PI;
    string name = "Nick Marriotti";
    char gender = 'M';
    bool isMale = false;

    cout << "Age is " << age << endl;
    cout << "Money is " << money << endl;
    cout << "Pi is " << pi << endl;
    cout << "Your name is " << name << endl;
    cout << "Gender is " << gender << endl;

    if(gender == 'M') {
        isMale = true;
    }

    if(isMale) {
        cout << "You are male!";
    }

    return 0;
}
