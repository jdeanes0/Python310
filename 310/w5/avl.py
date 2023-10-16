"""
Uh oh. We're doing something complicated.

@author jdeanes0
@version 10/16/23
"""

import bst

class AVLNode(bst.Node):
    """
    Node that inherits the properties of the original node.
    However, this also tracks height.
    """
    height = 0 # starts at 1 because if it exists, then it must be 1. Actually, I have no clue.

    def __init__(self, value, left=None, right=None):
        """Constructor function, can be called with detailed children or without detailed children"""
        super().__init__(value, left, right)
        self.height = 1 # Yeah this isn't fully working yet. I'm just surprised at how there aren't any errors.

class AVLTree(bst.Tree):
    """
    General object for accessing the nodes
    Do I dare to try this?
    """
    count = 0
    root = None # of type node

    def make_node(self, element):
        self.count += 1
        return AVLNode(element)
    
    def update_heights():
        pass
    
    def insert(self, value):  # this is the function that gets called, pay attention that we're not sending `root`
        if self.root is None:
            self.root = AVLNode(value)
            self.count = 1
            # if there is no root, there is no need to update the heights
        else:
            self._insert(self.root, value) # here's the call to a "private" function to which we are passing nodes down, starting from root

