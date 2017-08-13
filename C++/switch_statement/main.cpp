#include <iostream>

using namespace std;

int main()
{
    int choice;

    cout << "Enter selection (1-3) => ";
    cin >> choice;

    switch(choice) {
        case 1:
            cout << "You chose 1" << endl;
            break;
        case 2:
            cout << "You chose 2" << endl;
            break;
        case 3:
            cout << "You chose 3" << endl;
            break;
        default:
            cout << "Invalid option." << endl;

    }

    return 0;
}
