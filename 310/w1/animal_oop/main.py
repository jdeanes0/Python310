"""Runs the object-oriented code as a kind of test"""

from horse import Horse
from goat import Goat
from pig import Pig

herbert = Horse(900, "red", 35)

herbert.eat()
herbert.speak()
herbert.race()

goaty = Goat(220, "sueve")
piggy = Pig(1000, "tan")

goaty.climb()
goaty.speak()

piggy.mudbathe()
