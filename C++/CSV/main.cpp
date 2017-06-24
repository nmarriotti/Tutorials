#include <iostream>
#include <fstream>
#include <string>

using namespace std;


int main()
{
  string line;
  string filename;

  string firstName;
  string lastName;
  string gender;
  int age;

  cout << "Input file: ";
  cin >> filename;

  std::ifstream myfile(filename.c_str());
  if (myfile.is_open())
  {
    while ( getline (myfile,line) )
    {
      getline(myfile,firstName,',');
      cout << firstName;
    }
    myfile.close();
  }

  else cout << "Unable to open file";


    return 0;
}
