# 2. Polymorphism
# Drived classes can behave differently for the same method inherited from a base class.
# With polymorphism, a method name can mean different things across multiple classes.
# Example : Imagine a `speak()` method. DOgs `bark()`, while cats `meow()`, even thugh both use `speak`

class Dog:
    def speak(self):
        return 'Woof!'
    
class Cat:
    def speak(self):
        return 'Meow!'
    
# polymorphism in action
for animal in [Dog(), Cat()]:
    print(animal.speak())