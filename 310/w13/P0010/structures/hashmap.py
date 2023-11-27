"""
Contains the implementation for the required Hash Map.

@author jdeanes0
@version 11/27/23
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
        self.buckets = 0
        self.size = 997
        self.table = [LL() for _ in range(self.size)]

    def return_load(self):
        return self.buckets / self.size

    def find(self, title: str) -> bool:
        """Prints out all entries for a particular movie name"""
        title = self.__get_first_words(title)

        bucket = self.table[self.__hash(title)]
        if bucket.head is None:
            return False # early exit if the movie does not exist.
        
        bucket.find(title)

        # there_are_movies_left = True
        # last_out = ""
        # out = ""
        # while there_are_movies_left: # Ok but look at this steve. Look at this readability!!! It literally doesn't get better than this!!!
        #     there_are_movies_left, out = bucket.find(title)
        #     if out == last_out:
        #         return True # Done printing if we get duplicate outputs.

        #     print(out)
        #     last_out = out
        return True

    def add(self, r: Record):
        """Adds a Record to the table"""
        title = self.__get_first_words(r.get_movie())

        target = self.__hash(title)
        if self.table[target].head is None: # Increment buckets for later use if one is being created.
            self.buckets += 1

        # Add to the already-present linked list
        existinglist = self.table[target]
        existinglist.add(r)

        self.table[target] = existinglist

        self.count += 1
        # Increment count for later

    def delete(self, title: str) -> bool:
        """
        Goes to a specific hash to delete all movies in the hash.
        
        The title has to be EXACT or the quotes will not be found.
        """

        # Check if the specified movie exists in that bucket
        title = self.__get_first_words(title)

        target = self.__hash(title)
        if self.table[target].head is None:
            return False # Return False upon not finding the bucket.
        
        # At this point, the movie exists AND there are buckets to go through.

        there_are_movies_left = True
        while there_are_movies_left: # Ok but look at this steve. Look at this readability!!! It literally doesn't get better than this!!!
            there_are_movies_left = self.table[target].delete_by_movie(title)
            self.count -= 1

        if self.table[target].head is None: # If the result of the repeated deletions clears the bucket, update it.
            self.buckets -= 1

        return True # Delete until there are none left, and return True for success

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
                returnable += "index " + str(loc) + ": " + str(i) + "\n"
            loc += 1

        return returnable
