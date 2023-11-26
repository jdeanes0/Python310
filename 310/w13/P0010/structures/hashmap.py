"""
Contains the implementation for the required Hash Map.

@author jdeanes0
@version 11//23
"""

from structures.record import Record
from structures.linkedlist import LL

class HashMap:
    """
    Class containing the required functionality of a Linked-List Hash Map.

    Contains:
    hash(k)
    add(v)
    delete(v)
    find(v)
    count() -> int
    """

    def __init__(self):
        self.count = 0
        self.size = 997
        self.table = [LL() for _ in range(self.size)]

    def find(self, title: str):
        """Prints out all entries for a particular movie name"""
        title = self.__get_first_words(title)

        s = self.table[self.__hash(title)]

        if s.head is not None:
            print(s)
        else:
            print("Could not find requested movie.")

    def add(self, r: Record):
        """Adds a Record to the table"""

        target = self.__hash(r.get_movie())
        print("target:", target)
        # Add to the already-present linked list
        print("add to existing")
        existinglist= self.table[target]
        existinglist.add(r)

        self.table[target] = existinglist

        self.count += 1
        # Increment count for later

    def __get_first_words(self, title:str) -> str:
        """
        Returns the first two words of a string.
        """

        tokens = title.split(" ")
        if len(tokens) < 3:
            return title
        else: # If there are 3 or more tokens, return the first two tokens concatenated.
            returnable = ""
            count = 0
            for token in tokens:
                count += 1

                returnable += token + " "
                if count == 2:
                    return returnable

    def __hash(self, title: str) -> int:
        """
        Hashes the first two words of the title of the movie
        """
        # Get the first two tokens of the movie.
        title = self.__get_first_words(title)

        return hash(title) % self.size
    
    def get_count(self):
        """Returns the number of elements in the hashmap"""
        return self.count

    def __str__(self) -> str:
        """Prints out all tables in the hash map"""
        returnable = ""
        loc = 0
        for i in self.table:
            if i.head is not None:
                print("found an entry")
                returnable += "index " + str(loc) + ": " + str(i) + " "
            loc += 1

        return returnable
