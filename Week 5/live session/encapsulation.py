# 3. Encapsulation
# This practice of keeping attributes and methods private to prevent unwanted interference from outside the class.
# It's like hiding your chocolate 🍫 stash from everyone else.

class SecretStash:
    def __init__(self):
        self.__chocolates = 10 # Private attribute.
    
    def take_chocolate(self):
        if self.__chocolates > 0:
            self.__chocolates -= 1
            print('One Chocolate taken! 😁')
        else:
            print('No chocolate left 🥺')

stash = SecretStash()
stash.take_chocolate()