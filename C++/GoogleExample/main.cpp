#include<iostream>
#include<unordered_set>
using namespace std;

int main() {
    int sum = 8;
    bool found = false;
    int list[4] = {1, 2, 9, 4};

    unordered_set<int> comp;
    for(int value : list) {
        if(comp.find(value) != comp.end()) {
            cout << "True" << endl;
            found = true;      
        }
        comp.insert(sum-value);
    }

    if(!found) 
        cout << "False" << endl;

    return 0;
}
