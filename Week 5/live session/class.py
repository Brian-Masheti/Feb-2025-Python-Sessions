class Car:
    color = "red"
    model = "Bentley"

    # method/behavior to display car details
    def drive(self): # Self 
        print("The car is driving 🚗")
    def stop(self):
        print('The Car has stopped 🛑')

my_car = Car()  # create an instance of the Car class
my_car.drive()  # call the drive method. We have to include self in the drive function i.e., def drive(self) for it run.
my_car.stop() # Call the stop method
print(my_car.color)  # access the class variable color

print(my_car.model)  # access the class variable model

# Self is just like a pointer which refers to the instance of the class the method is in.
# Self refers to the instance of the class and is used to access attributes and methods with the class.




# Constructors: The __init__ Method and instance variables 🚀
# __init__ method allows each objectto start with specific values.


class Car:
    def __init__(self, color, model):
        self.color = color  # Instance variable
        self.model = model  # Instance variable

# Creating objects with unique attributes
car1 = Car('blue', 'Sedan')
car2 = Car('red', 'SUV')

print(car1.color)   # Output: blue
print(car2.model)   # Output: SUV



class Person:
    # Constructor method to initialize the object.
    def __init__(self, name, age, height):
        self.name = name # nstance varable for name
        self.age = age # instance variable for age
        self.height = height
        
personDetails = Person('John', 30, 1.79) # Create an instance of the person class
print(personDetails.name) 





