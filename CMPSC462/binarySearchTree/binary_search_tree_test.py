from binary_search_tree_v2 import BinarySearchTreeNode, build_tree, is_binary_search_tree, merge_trees
import random

# Testing binary search tree functions
vals = random.sample(range(1,50), 25)
t = build_tree(vals)

#insertion
t.insert(357)

# in order
print(t.in_order_traversal(), end="\n") # note that '357' now appearsin the list

# pre order traversal
print(t.pre_order_traversal(), end="\n")

# post order traversal
print(t.post_order_traversal(), end="\n")

# finding a node
print(t.search(vals[4]), end="\n") # finding a random val in t

# min and max
print(f"Min: {t.min()}")
print(f"Max: {t.max()}", end="\n")
print(f"\nDo they work?: Max={t.max()==sorted(t.in_order_traversal())[-1]} min={t.min()==sorted(t.in_order_traversal())[0]} ")

# removal
t.delete(357)
print(t.in_order_traversal(),end="\n\n\n\n")
print(f"357 in t == {357 in t.in_order_traversal()}\n")

#generating and randomizing values
evens = random.sample([i for i in range(0,50) if i % 2 == 0], 25)
odds = random.sample([i for i in range(0,50) if i % 2 != 0], 25)



# creating trees from those values
even_tree = build_tree(evens)
odd_tree = build_tree(odds)


# merging the trees
#combined = merge_trees(even_tree, odd_tree)
print(even_tree.in_order_traversal())
print(odd_tree.in_order_traversal())

combined = merge_trees(even_tree,odd_tree)
print(combined.in_order_traversal())