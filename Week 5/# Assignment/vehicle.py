# Part II: Polymorphism Challenge
# This program demonstrates polymorphism with vehicles
# Each vehicle type implements the move() method differently

class Vehicle:
    """
    Constructor to initialize vehicle name
    """
    def __init__(self, name):
        self.name = name  # Public attribute: vehicle name

    """
    Generic move method (to be overridden by subclasses)
    """
    def move(self):
        return f"{self.name} is moving."


class Car(Vehicle):
    """
    Override move method for Car
    """
    def move(self):
        return f"{self.name} is driving on the road. 🚗"


class Plane(Vehicle):
    """
    Override move method for Plane
    """
    def move(self):
        return f"{self.name} is flying in the sky. ✈️"


class Boat(Vehicle):
    """
    Override move method for Boat
    """
    def move(self):
        return f"{self.name} is sailing on the water. ⛵"


# Test polymorphism
if __name__ == "__main__":
    """
    Create a list of different vehicles
    """
    vehicles = [
        Car("Toyota Camry"),
        Plane("Boeing 747"),
        Boat("Sailor’s Dream")
    ]

    """
    Call move() on each vehicle to demonstrate polymorphism
    """
    for vehicle in vehicles:
        print(vehicle.move())