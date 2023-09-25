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
    data = None
    left = None
    right = None

    def __init__(self, data, left=None, right=None):
        """Constructor function, can be called with detailed children or without detailed children"""
        self.data = data
        self.left = left
        self.right = right

class Tree:
    """General object for accessing the nodes"""
    count = 0
    root = None # of type node

    def addagain(self, root: Node, element):
        """Why can't python find this function?"""
        print("hey?")
        if element <= root.data:
            pass

    def add(self, element):
        if self.count == 0:
            self.root = Node(element)
            self.count = 1
        else:
            addagain(self.root, element)
    