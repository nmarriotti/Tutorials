# TITLE:       User input in Python
# DESCRIPTION: Stores user input into variables and outputs the variables
#              to the user.

def main():
    name = input('What is your name? ')
    age  = input('How old are you? ')
    # output
    print('Hello', name, ' you are', age)

if __name__ == "__main__":
    main()
