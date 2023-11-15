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
        self.hash(r.get_movie())
        self.count += 1

    def hash(self, title: str) -> int:
        """
        Hashes the title of the movie
        """

        # I don't know what to do here..... How do I hash this?
