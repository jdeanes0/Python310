"""
Class to hold the multi-mapping data structure for the hash map, a linked list.
The linked list uses records as their nodes.

@author jdeanes0
@version 11/14/23
"""

from record import Record

class Node:
    """
    Simple node class.
    
    Uses the record object to store data.
    """

    data: Record

    def __init__(self, r: Record):
        """Creates a node"""
        self.data = r
        self.next = None

class LL:
    """
    Simple linked list class.
    """

    head = None
    count: int

    def __init__(self):
        """Creates a linked list"""
        self.head = None
        self.count = 0

    def add(self, r: Record):
        """
        Adds a value to the beginning of the linked list (Efficiency!)

        :param r: A record object containing a single movie quote and its data.
        """

        if self.count == 0:
            self.head = Node(r)
            self.count = 1
        else:
            old_head = self.head # Store the old linked list inside of a variable
            self.head = Node(r) # Newest node becomes the head
            self.head.next = old_head # Set the new head's node to the rest of the linked list
            self.count += 1
    
    def delete(self, r: Record):
        """
        Deletes an element from a list
        """
        pass

    def find(self, moviequote: str) -> bool:
        """
        Checks to see if a item is in a list
        """

        # Traveler!
        tv = self.head
        while tv: # will traverse as long as the node is not None
            if moviequote.lower() in tv.data.get_quote().lower():
                print(tv.data)
                return True
            # The movie was found and printed, leave the list and let the HashMap know as well with the True return
            tv = tv.next

        return False # If the movie is not found, return false.
