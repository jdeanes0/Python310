"""Replacement class for the Stack.py that my OneDrive lost"""

class Stack:
    """Steve said so."""

    __count = 0
    __dat = []

    def __init__(self, length: int):
        """Constructs an empty stack of the length provided"""

        self.__dat = [None]*length # guaranteed to be a list of 0s

    def push(self, e):
        """Pushes a single element to the list.
        TODO: Returns false upon failure."""
        if self.__count == len(self.__dat):
            return False

        self.__dat[self.__count] = e
        self.__count += 1

        return True

    def pushList(self, elist):
        """Adds an entire list to the stack but will return false if there is a lack of available space."""
        if (len(elist) + self.__count) > len(self.__dat):
            # If the new list plus the list of stack elements is longer than the list was initialized to handle:
            return False

        for e in elist: # For every element in the list that will be added
            self.__dat[self.__count] = e # add the element to the stack
            self.__count += 1 # increment the count of elements by one
        return True

    def pop(self):
        """Returns the element at the top of the stack"""
        to_return = self.__dat[self.__count - 1]
        self.__count -= 1

        return to_return

    def peek(self):
        """Looks at and returns the top of the stack"""
        return self.__dat[self.__count - 1]

    def count(self):
        """Returns the number of elements in the stack"""
        return self.__count

    def __str__(self):
        to_return = ""
        for i in range(self.__count): # Iterate over the length of the stack and just start appending values
            to_return += f"{self.__dat[i]}\t"
        return to_return
