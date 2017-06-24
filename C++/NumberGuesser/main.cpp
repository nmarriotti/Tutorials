#include <iostream>
#include <cstdlib>
#include <time.h>

using namespace std;

// Declare Function
bool checkNum(int, int);

int main()
{
    // Generate a random number 1-10
    srand (time(NULL));
    int answer = rand() % 11;

    // Create variable to store users guess
    int guess;

    do {

      // Tell user to guess a number
      cout << "Enter a number 1-10: ";

      // Store the users guess
      cin >> guess;

      // Check if the user is right
      if(checkNum(guess, answer)) {
        cout << "You win!\n";
      } else {
        cout << "Try again!\n";
      }

      // Loop until you win!
    } while (answer != guess);

    // Exit
    return 0;
}

// Check if the users guess is right.
bool checkNum(int userGuess, int answer) {
    if(userGuess == answer) {
        // You win!
        return true;
    } else {
        // Try again!
        return false;
    }
}
