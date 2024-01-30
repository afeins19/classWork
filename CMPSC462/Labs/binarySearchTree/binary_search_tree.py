"""
DocViewer
Pages
Assignment-5 (30 points)
Binary Search Tree
Exercise-1: (15 points)
Develop a BinarySearchtree.py which can perform the following functions:
 Insert node to a tree
 Perform In-order traversal
 Perform Pre-order traversal
 Perform Post-order traversal
 Find a node
Exercise-2: (15 points)
Write a function to remove a node from a tree data structure? This function should consider all
the three cases: case-1: remove a leaf node, case-2: remove a node with one child and case-3:
remove a node with two children.
Perform the time complexity for this function. Briefly explain?
Annotations
"""

"""Time Compleixty:
    Worst Case: Unbalanced Tree - O(n)
        - as this tree is completely unbalanced, it essentially functions as a linked list so we traverse it linearly 

    Best Case/Average Case: Balanced Tree - O(logn)
        - here we can actually get some utility out of the tree. We can reduce the path length of our traversal given 
        that we balance our tree  
"""

class Node:
    def __init__(self, data, l_child = None, r_child = None):
        self.data = data
        self.l_child = l_child
        self.r_child = r_child

    def __eq__(self, other):
        return self.data == other.data

    def __gr__(self, other):
        return self.data > other.data

    def __lt__(self, other):
        return self.data < other.data

class bst:
    def __init__(self, root: Node):
        self.root = root
        self.l = None
        self.r = None


root = Node(12)
tree = bst(root)
tree.insert(tree.root, 5)
print(root.l_child)

















