# The __init__.py inside this folder tells Python a file can be imported from this directory

class Person():

    # This __init__ AKA initialize method is called everytime a person object is created
    def __init__(self, input_name):
        self.hidden_name = input_name

    # Returns the persons name
    def getName(self):
        print('inside the getter')
        return self.hidden_name

    def setName(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name

    name = property(getName, setName)
