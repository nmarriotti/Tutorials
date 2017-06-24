# Main.py
# This is the main program and will read from the PersonClass.py file


# Import Person class so we can use the code it contains
# classes.person refers classes folder and person.py file and we are
# importing the class Person
from classes.person import Person

def main():

    # Create an empty array.
    PersonList = []

    # Create some objects from the Person class
    person1 = Person(input('Enter a persons name: '))
    person2 = Person(input('Enter a persons name: '))
    person3 = Person(input('Enter a persons name: '))

    # Add each person object to the PersonList array
    PersonList.append(person1)
    PersonList.append(person2)
    PersonList.append(person3)

    # Check the length of the array. str() converts the number to a string
    print('The length of the array is: ' + str(len(PersonList)))

    # Get the name of the people we just created using a for loop and calling
    # the getName method from the Person class
    for items in PersonList:
        print(items.getName())


if __name__ == "__main__":
    main()
