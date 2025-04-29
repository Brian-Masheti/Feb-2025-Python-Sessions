# Assignment Part I
# This program defines a Superhero class and a FlyingSuperhero subclass
# Demonstrates attributes, methods, constructors, encapsulation, and inheritance

class Superhero:
    # Constructor to initialize a superhero object
    def __init__(self, name, power, health):
        self.name = name  # Public attribute: superhero's name
        self.power = power  # Public attribute: superhero's main power
        self.__health = health  # Private attribute: superhero's health (encapsulation)

    # Method to use the superhero's power
    def use_power(self):
        return f"{self.name} uses {self.power}!"

    # Method to reduce health when superhero takes damage
    def take_damage(self, damage):
        self.__health -= damage  # Access private health attribute
        if self.__health < 0:
            self.__health = 0
        return f"{self.name} takes {damage} damage. Health now: {self.__health}"

    # Method to display superhero's current status
    def get_status(self):
        return f"Name: {self.name}, Power: {self.power}, Health: {self.__health}"


class FlyingSuperhero(Superhero):
    # Constructor for FlyingSuperhero, extending Superhero
    def __init__(self, name, power, health, flight_speed):
        super().__init__(name, power, health)  # Call parent class constructor
        self.flight_speed = flight_speed  # New attribute: flight speed

    # Override use_power method to include flying (polymorphism)
    def use_power(self):
        return f"{self.name} flies at {self.flight_speed} mph and uses {self.power}!"

    # New method specific to FlyingSuperhero
    def fly(self):
        return f"{self.name} soars through the sky at {self.flight_speed} mph!"


# Test the classes
if __name__ == "__main__":
    # Create a regular superhero
    hero = Superhero("Captain Strength", "Super Strength", 100)
    print(hero.get_status())  # Show initial status
    print(hero.use_power())  # Use power
    print(hero.take_damage(20))  # Take damage
    print(hero.get_status())  # Show updated status

    # Create a flying superhero
    flying_hero = FlyingSuperhero("Sky Blazer", "Laser Vision", 120, 200)
    print("\n" + flying_hero.get_status())  # Show initial status
    print(flying_hero.use_power())  # Use overridden power method
    print(flying_hero.fly())  # Use fly method
    print(flying_hero.take_damage(30))  # Take damage
    print(flying_hero.get_status())  # Show updated status