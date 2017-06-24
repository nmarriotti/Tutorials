################################################################################
# TITLE:       Using Methods in Python
# DESCRIPTION: Stores user input into variables and outputs the variables
#              to the user.
################################################################################

# Need to include this to get the current date/time
from datetime import datetime


# MAIN METHOD
def main():
    name = input('What is your name? ')
    birthYear  = input('What year were you born (4-digit)? ')
    print('Hello',name)
    # CALL METHOD 2 and return how old you are
    print('You are',calculateAge(birthYear))
    print('Bye!')


# METHOD 2
def calculateAge(x):
    # Get the current date
    now = datetime.now()
    # Get the current year
    currentYear = now.year
    # Figure out how old they are and convert x into a whole number variable
    yourAge = currentYear - int(x)
    # Send your age back to where it was called from using return
    return yourAge


if __name__ == "__main__":
    # Here we start the program by calling the main method
    main()
