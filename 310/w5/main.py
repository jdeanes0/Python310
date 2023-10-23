# import bst

# testing_tree = bst.Tree()

# testing_tree.insert(5)
# testing_tree.insert(6)
# testing_tree.insert(77)
# testing_tree.insert(85)
# testing_tree.insert(59)
# testing_tree.insert(10)
# testing_tree.insert(1)
# testing_tree.insert(544)

# try:
#     print("We found", testing_tree.find(545))
# except:
#     print("We did not find the number")

# print("count:", testing_tree.count)

# print("preorder:", testing_tree.preorder())
# print("inorder:", testing_tree.inorder())
# print("postorder:", testing_tree.postorder())

import avl

test_avl_tree = avl.AVLTree()

test_avl_tree.insert(5)
test_avl_tree.insert(6)
test_avl_tree.insert(77)
test_avl_tree.insert(85)
test_avl_tree.insert(59) # only involves a left rotate

test_avl_tree.insert(10) # works up to the point of inserting 10, after which everything breaks. # seems to also add a right rotate then a left rotate.

# But now it can't find 544?
test_avl_tree.insert(1)
test_avl_tree.insert(544) # Why is this a triple rotate? This is like a single one. WTF? l77 is correct, l6 and r59 are both wrong.
# Time for a debug dive.
test_avl_tree.insert(52)

print("count:", test_avl_tree.count)

print("preorder:", test_avl_tree.preorder())
print("inorder:")
test_avl_tree.print_inorder_with_heights() # This is actually a great debug function, I am thoroughly impressed.
print("height:", test_avl_tree.root.height) # These need to be from the Tree class.
