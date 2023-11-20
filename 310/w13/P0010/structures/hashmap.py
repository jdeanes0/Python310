"""
Contains the implementation for the required Hash Map.

@author jdeanes0
@version 11/14/23
"""

from record import Record
from linkedlist import LL

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

    count = 0
    table = [LL]*997

    def add(self, r: Record):
        """Adds a Record to the table"""
        self.table[self.hash(r.get_movie())] = r
        self.count += 1

    def hash(self, title: str) -> int:
        """
        Hashes the first two words of the title of the movie
        """
        # Get the first two tokens of the movie.


        return hash(title)
        # I don't know what to do here..... How do I hash this?

    def tokenize(self, title: str) -> str:
        """
        Return the first two tokens in the movie title.

        :param title: A full movie title
        :return: The first two tokens as a string.
        """

        line = str.split(title, " ")



        return final

    