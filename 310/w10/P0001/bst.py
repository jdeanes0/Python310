"""
I think that I'm just going to take my notes in VSCODE now for 310
Why? It's honestly just a practical choice.
Like, code is so important to this course with making these data structures.

9/25/23: Trees
Trees have leaves, nodes, and a root (self-explanatory)

BSTs: Trees that only have 0-2 children per node
n-ary (Mary) tree: Trees that can have any base number of children per node

Traversal: preorder, inorder, postorder (DFS) also these are basically stacks
         : queue-search (BFS)
Searching: Depth-first search (DFS) & Breadth-first search (BFS)

When moving about a tree, each node, not the data for the node, is put into a data structure.
That way, the objects themselves can be accessed easily

@author jdeanes0
@version 10/15/23
"""

import kvpair
import music

class Node:
    """Object that holds the node data"""
    value:kvpair.KVPair = kvpair.KVPair(music.Music(None, None, None, None))
    left = None
    right = None

    def __init__(self, value:music.Music, left=None, right=None):
        """Constructor function, can be called with detailed children or without detailed children"""
        self.value = kvpair.KVPair(value)
        self.left = left
        self.right = right

class Tree:
    """General object for accessing the nodes"""
    count = 0
    root = None # of type node

    def make_node(self, element):
        self.count += 1
        return Node(element)

    def insert(self, value):  # this is the function that gets called, pay attention that we're not sending `root`
        if self.root is None:
            self.root = Node(value)
            self.count = 1
        else:
            self._insert(self.root, value) # here's the call to a "private" function to which we are passing nodes down, starting from root

    def _insert(self, node, value:kvpair.KVPair):
        # print(value) # Debug statement, leave here just in case tbh
        if value.get_key() < node.value.get_key():  # we know that `node` cannot be None - so it's safe to check its value! 
            if node.left:
                self._insert(node.left, value) # the recursive call is done only when `node.left` is not None
            else:
                node.left = self.make_node(value)
        else:
            if node.right:
                self._insert(node.right, value)
            else:
                node.right = self.make_node(value)

    def __preorder(self, root:Node|None) -> str:
        """Performs a preorder traversal on the tree for the purpose of debugging"""
        if root is None:
            return ""
        
        return str(root.value.get_key()) + " | " + self.__preorder(root.left) + self.__preorder(root.right)
    
    def preorder(self):
        """Returns the preorder traversal of the tree"""
        if self.root is None:
            return ""

        return self.__preorder(self.root)
    
    def __inorder(self, root:Node|None) -> str:
        """Performs an inorder traversal on the tree for the purpose of debugging"""
        if root is None:
            return ""
        
        return "-" + self.__inorder(root.left) + "-" + str(root.value.get_key()) + "\n" + self.__inorder(root.right) + "-"
        
    def inorder(self):
        """Returns the inorder traversal of the tree"""
        if self.root is None:
            return ""

        return self.__inorder(self.root)
    
    def __postorder(self, root:Node|None) -> str:
        """Performs a postorder traversal of the tree for the purpose of debugging"""
        if root is None:
            return ""
        
        return self.__postorder(root.left) + self.__postorder(root.right) + str(root.value.get_key()) + " | "
    
    def postorder(self):
        """Returns the postorder traversal of the tree"""
        if self.root is None:
            return ""

        return self.__postorder(self.root)
    
    def printTree(self):
        self.__printTree(self.root)
    
    def __printTree(self, node, level=0):
        if node != None:
            self.__printTree(node.left, level + 1)
            print(' ' * 4 * level + str(level) + '-> ' + str(node.value.get_key()))
            self.__printTree(node.right, level + 1)
    
    def getCount(self):
        """Returns the count of the tree's nodes"""
        return self.count
    
    def find(self, e) -> kvpair.KVPair:
        """Find a key in a tree, return its value."""
        nodeval = self.__find(e, self.root).value # ...why is this none?
        if nodeval is None:
            raise Exception("ValueNotFound") # Don't return null. That's dumb.
        else:
            return nodeval
    
    def __find(self, e, root:Node|None) -> Node|None:
        """Recursively find the specified element
        Listen. This is a dumb method.
        However, it will be very useful when we need to use key-value pairs
        """
        the_node = None
        if root is None:
            return the_node # Return a null node if the root is empty
                              # Definitely hazardous, but this is what Steve did sooo
        elif e.lower() in root.value.get_key().lower():
            the_node = root
        elif e.lower() > root.value.get_key().lower():
            the_node = self.__find(e, root.right)
        elif e.lower() < root.value.get_key().lower():
            the_node = self.__find(e, root.left)
        
        return the_node
