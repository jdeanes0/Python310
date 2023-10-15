import tree

testing_tree = tree.Tree()

testing_tree.insert(5)
testing_tree.insert(6)
testing_tree.insert(77)
testing_tree.insert(85)
testing_tree.insert(59)
testing_tree.insert(10)
testing_tree.insert(1)
testing_tree.insert(544)

print("count: ", testing_tree.count)

print("preorder:", testing_tree.preorder())
print("inorder:", testing_tree.inorder())
print("postorder:", testing_tree.postorder())
