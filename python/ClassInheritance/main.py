class Car():
    def exclaim(self):
        print('I''m a car')

# Inherits everything inside the Car class
class Chevy(Car):
    pass



def main():
    # Create 2 objects
    object1 = Car()
    object2 = Chevy()
    # Call the exlaim method of the Car class
    object1.exclaim()
    object2.exclaim()


if __name__ == "__main__":
    main()
