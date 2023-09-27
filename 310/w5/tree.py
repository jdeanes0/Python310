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
@version 9/25/23
"""

class Node:
    """Object that holds the node data"""
    value = None
    left = None
    right = None

    def __init__(self, value, left=None, right=None):
        """Constructor function, can be called with detailed children or without detailed children"""
        self.value = value
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

    def _insert(self, node, value):
        print(value)
        if value < node.value:  # we know that `node` cannot be None - so it's safe to check its value! 
            if node.left:
                self._insert(node.left, value) # the recursive call is done only when `node.left` is not None
            else:
                node.left = self.make_node(value)
        else:
            if node.right:
                self._insert(node.right, value)
            else:
                node.right = self.make_node(value)
