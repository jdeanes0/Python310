"""
Class to hold the multi-mapping data structure for the hash map, a linked list.
The linked list uses records as their nodes.

@author jdeanes0
@version 11/26/23
"""

# from record import Record
from structures.record import Record

class Node:
    """
    Simple node class.
    
    Uses the record object to store data.
    """

    data: Record

    def __init__(self, r: Record):
        """Creates a node"""
        self.data = r
        self.next: None | Node = None

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

    def delete_by_movie(self, title: str) -> bool:
        """
        Will delete the first quote in the linked list that it sees from a particular movie.
        """
        # Traveler!
        tv = self.head # current node we're on
        target = None # node to be removed
        travel_count = 0 # keeps track of where we are in the linked list
        bridge = None # node after the target if it exists to set the next to be
        while tv:
            travel_count += 1
            if title.lower() in tv.data.get_movie().lower():
                target = tv
                bridge = tv.next
                break
            tv = tv.next
        
        if target: # If the node to be deleted exists, do work to delete it.
            # Special case for being the first in the linked list, just change self.head.
            if self.head == target:
                self.head = target.next
                return True

            # Now move to right before the element in question.
            tv2 = self.head
            while tv2:
                if tv2.next == target:
                    # If we have found the target, check if tv2.next.next exists
                    # If it does not, terminate at None.
                    if travel_count == self.count: # If the element to be deleted is at the end of the list
                        tv2.next = None
                    else:
                        tv2.next = bridge
                tv2 = tv2.next
            return True
        else:
            return False
    
    def delete(self, moviequote: str) -> bool:
        """
        Deletes an element from a list

        Navigates to the element to see if it exists, then navigates to the element before it to jump references.
        """
        # Traveler!
        tv = self.head # current node we're on
        target = None # node to be removed
        travel_count = 0 # keeps track of where we are in the linked list
        bridge = None # node after the target if it exists to set the next to be
        while tv:
            travel_count += 1
            if moviequote.lower() in tv.data.get_quote().lower():
                target = tv
                bridge = tv.next
                break
            tv = tv.next
        
        if target: # Special case for being the first in the linked list, just change self.head.
            if self.head == target:
                self.head = target.next
                return True

            # Now move to right before the element in question.
            tv2 = self.head
            while tv2:
                if tv2.next == target:
                    # If we have found the target, check if tv2.next.next exists
                    # If it does not, terminate at None.
                    if travel_count == self.count: # If the element to be deleted is at the end of the list
                        tv2.next = None
                    else:
                        tv2.next = bridge
                tv2 = tv2.next
            return True
        else:
            return False

    def find(self, title: str) -> bool:
        """
        Checks to see if a item is in a list
        """

        # Traveler!
        tv = self.head
        quotes_found = 0
        while tv: # will traverse as long as the node is not None
            if title.lower() in tv.data.get_movie().lower():
                print(tv.data)
                quotes_found += 1
            # The movie was found and printed, find more.
            tv = tv.next

        if quotes_found == 0:
            return False # If the movie is not found, return false.
        return True 
    
    def __str__(self) -> str:
        final = ""
        tv = self.head # Traveler to pass by nodes and record their contents.
        while tv:
            final += str(tv.data) + " "
            tv = tv.next
        return final
