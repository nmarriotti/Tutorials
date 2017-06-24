class Pet:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def getName(self):
        return self.name
    
    def gettype(self):
        return self.type

    def __str__(self):
        return "{} is a {}".format(self.name, self.type)

class Dog(Pet):
    def __init__(self, name, breed):
        Pet.__init__(self, name, "Dog")
        self.breed = breed

    def getBreed(self):
        print(self.breed)



def main():
    Buddy = Dog("Buddy", "Golden Retriever")
    print(Buddy)
    Buddy.getBreed()

    Max = Dog("Max", "Pug")
    print(Max)
    Max.getBreed()

if __name__ == "__main__":
    main()