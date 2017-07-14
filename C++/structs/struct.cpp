#include <iostream>
#include <string>
using namespace std;

int main() {

    struct Contact {
        string name;
        int age;
    }typedef Contact;

    Contact nick = {"Nick",29};

    cout << nick.name << endl;

    return 0;
}