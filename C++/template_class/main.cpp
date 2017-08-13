#include <iostream>

using namespace std;

/*
Class templates allow you to pick which data type is used for variables.
*/

template <typename TYPE1=int, typename TYPE2=double> /* Default is int, double */
class Example {
    private:
        TYPE1 value1;
        TYPE2 value2;

    public:
        Example(TYPE1 val1, TYPE2 val2) {
            cout << "Constructor" << endl;
            value1 = val1;
            value2 = val2;
        }

        TYPE1 get_value1() {
            return value1;
        }

        TYPE2 get_value2() {
            return value2;
        }
};

int main()
{
    Example<> object1 (29, 49.99); /* use default data types */
    cout << object1.get_value1() << endl;
    cout << object1.get_value2() << endl;

    Example<int, string> object2 (29, "Learning templates in C++"); /* use int, string data type */
    cout << object2.get_value1() << endl;
    cout << object2.get_value2() << endl;


    return 0;
}
