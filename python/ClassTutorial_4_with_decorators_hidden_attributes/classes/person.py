# The __init__.py inside this folder tells Python a file can be imported from this directory

class Person():

    # This __init__ AKA initialize method is called everytime a person object is created
    def __init__(self, input_name):
        self.__name = input_name

    # Returns the persons name
    @property
    def name(self):
        print('inside the getter')
        return self.__name

    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.__name = input_name
