# OOP principles: Inheritance, Polymorphism, and Encapsulation.
# Inheritance - Just like humans, classes can also inherit attrbutes and methods from other classes. 
# This helps reduce code repetition and create a natural hierarchy of code.

# 1. Inheritance
class Vehicle:
    def __init__(self, wheels):
        self.wheels = wheels

class Car(Vehicle):
    pass

car = Car(4)
print(car.wheels) # utput: 4