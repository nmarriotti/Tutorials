################################################################################
# TITLE:       Arrays in Python
# DESCRIPTION: How to use store multiple items in the same variable
################################################################################


def main():

    print('This is an example of an Array')
    # index     0        1        2      3
    people = ['Nick', 'Steve', 'John', 'Mary']
    print(people[2]) # 2 is referring to string at index 2 which is John
    print(people[0])


    print('This is an example of a two-dimensional Array')
    # group             0                          1
    #         -------------------------------------------------
    # index     0       1      2         0         1        2
    colors = ['blue','white','red'], ['quarter', 'half', 'full']
    print(colors[1][2])
    print(colors[0][0])



if __name__ == "__main__":
    # Here we start the program by calling the main method
    main()
