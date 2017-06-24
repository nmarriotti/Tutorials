################################################################################
# TITLE:       Loops in Python
# DESCRIPTION: Do something until a condition is false
################################################################################


def main():
    i = 0

    print('This is an example of a while loop.')
    while i < 10:   # Check if i is still less then 10
        print(i)    # print i
        i += 1      # add 1 to i and
                    # repeat

    people = ['Nick', 'Steve', 'John', 'Mary']
    print('This is an example of a for loop.')
    for item in people:     # Output each person in the people array
        print(item)         # print
                            # repeat



if __name__ == "__main__":
    # Here we start the program by calling the main method
    main()
