#include <iostream>

using namespace std;

class People {

private:
    string name;
    int age;

public:
    People(string inputName, int inputAge) {
        // Constructor
        name = inputName;
        age = inputAge;
        cout << "Created a new People object" << endl;
    }

    void getName() {
        cout << "My name is " << name << endl;
    }

    void setName(string newName) {
        name = newName;
    }

};


int main()
{
    People new_person("Nick", 28);
    new_person.getName();
    new_person.setName("Stephanie");
    new_person.getName();
    return 0;
}
