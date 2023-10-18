import bst

testing_tree = bst.Tree()

testing_tree.insert(5)
testing_tree.insert(6)
testing_tree.insert(77)
testing_tree.insert(85)
testing_tree.insert(59)
testing_tree.insert(10)
testing_tree.insert(1)
testing_tree.insert(544)

try:
    print("We found", testing_tree.find(545))
except:
    print("We did not find the number")

print("count:", testing_tree.count)

print("preorder:", testing_tree.preorder())
print("inorder:", testing_tree.inorder())
print("postorder:", testing_tree.postorder())

# import avl

# test_avl_tree = avl.AVLTree()

# test_avl_tree.insert(5)
# test_avl_tree.insert(6)
# test_avl_tree.insert(77)
# test_avl_tree.insert(85)
# test_avl_tree.insert(59)
# test_avl_tree.insert(10)
# test_avl_tree.insert(1)
# test_avl_tree.insert(544)

# print("count:", test_avl_tree.count)

# print("preorder:", test_avl_tree.preorder())
# print("inorder:", test_avl_tree.inorder())
# print("height:", test_avl_tree.root.height) # These need to be from the Tree class.
