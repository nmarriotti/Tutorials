# The __init__.py inside this folder tells Python a file can be imported from this directory

class Person():

    # This __init__ AKA initialize method is called everytime a person object is created
    def __init__(self, name):
        self.name = name

    # Returns the persons name
    def getName(self):
        return self.name
