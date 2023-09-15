"""
@author jdeanes0
Parent class for the sample UML demonstration
"""

from hair import Hair

class Animal:
    """Class representing an animal"""
    weight = None
    hair = None

    def __init__(self, weight, haircolor):
        self.weight = weight
        self.hair = Hair(haircolor) # hair becomes an object of type hair with a color
    
    def eat(self):
        """Says that the animal is eating"""
        print("The animal is eating.")
        return self

    def speak(self):
        """The animal is very vain and tells you what color hair it has"""
        print("I have " + self.hair.color + " hair.")
        return self

# haircolor = "green"
# small_horse = Animal(350, haircolor)
# print(small_horse.weight)
# small_horse.speak()
# small_horse.eat()
