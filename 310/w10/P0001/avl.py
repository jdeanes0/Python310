"""
Uh oh. We're doing something complicated.

@author jdeanes0
@version 10/16/23
"""

import bst
import kvpair
import music

class AVLNode(bst.Node):
    """
    Node that inherits the properties of the original node.
    However, this also tracks height.
    """
    height = 0 # starts at 1 because if it exists, then it must be 1. Actually, I have no clue.

    def __init__(self, value:kvpair.KVPair, left=None, right=None):
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
    
    def get_height(self, root):
        """Get the height of the node specified"""
        if root is None:
            return 0
        return root.height
    
    def insert(self, value):  # this is the function that gets called, pay attention that we're not sending `root`
        """Attempt to insert a value into the tree"""
        print("Adding " + str(value))
        if self.root is None:
            self.root = AVLNode(value)
            self.count = 1
            print(self.count, self.get_height(self.root))
            # if there is no root, there is no need to update the heights
        else:
            self.root = self._insert(self.root, value) # here's the call to a "private" function to which we are passing nodes down, starting from root
            print(self.count, self.get_height(self.root))
            # self._insert(self.root, value)

    def _insert(self, node:AVLNode, value:music.Music):
        """Find where the newly created node will go in the tree"""
        # print(value) # Debug statement, leave here just in case tbh
        if value.get_title() < node.value.get_key():  # we know that `node` cannot be None - so it's safe to check its value! 
            if node.left:
                node.left = self._insert(node.left, value) # the recursive call is done only when `node.left` is not None
            else:
                node.left = self.make_node(value)
        else:
            if node.right: # if it exists
                node.right = self._insert(node.right, value)
            else:
                node.right = self.make_node(value)

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        # WARNING: DANGEROUS AVL NONSENSE BELOW

        # Set up potential right rotations
        balance_amt = self.determine_balance(node)
        if balance_amt > 1:
            if value.get_title() < node.left.value.get_key():
                node = self.right_rotate(node)
            else:
                node.left = self.left_rotate(node.left)
                node = self.right_rotate(node)
            
        # Set up potential left rotations
        if balance_amt < -1:
            if value.get_title() >= node.right.value.get_key():
                node = self.left_rotate(node)
            else:
                node.right = self.right_rotate(node.right)
                node = self.left_rotate(node)

        return node
            

    def determine_balance(self, root):
        if root is None:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)
    
    def left_rotate(self, root):
        """Performs a left rotation"""
        
        print("left rotate has occurred on root node " + str(root.value.get_key()))
        
        # reference switch
        y = root.right
        tmp = y.left # root.right.left
        y.left = root
        root.right = tmp
        # print(self.preorder())

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def right_rotate(self, root):
        """Performs a right rotation"""
        
        print("right rotate has occurred on root node " + str(root.value.get_key()))

        # reference switch
        # print("root's type is:", type(root))

        y = root.left

        # print("y's type is:", type(y)) # Why are nodes being lost?
        tmp = y.right
        y.right = root
        root.left = tmp

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y
    
    def __print_inorder_with_heights(self, root):
        """Interior function, should not be seen by the user"""
        if root is None:
            return
        
        self.__print_inorder_with_heights(root.left)        
        print(str(root.value.get_key())+"_h"+str(root.height)+" ")
        self.__print_inorder_with_heights(root.right)
    
    def print_inorder_with_heights(self):
        """Debugging levels that shouldn't even be possible"""
        self.__print_inorder_with_heights(self.root)
