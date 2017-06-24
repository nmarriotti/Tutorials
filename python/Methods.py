################################################################################
# TITLE:       Using Methods in Python
# DESCRIPTION: Get the users name in one method and outputs it using another.
################################################################################



# MAIN METHOD
def main():
    name = input('What is your name? ')
    age  = input('How old are you? ')
    # CALL OUTPUT METHOD and pass it the name and age
    output(name, age)


# OUTPUT METHOD
def output(x, y):
    print('Hello', x,'you are', y)


if __name__ == "__main__":
    # Here we start the program by calling the main method
    main()
