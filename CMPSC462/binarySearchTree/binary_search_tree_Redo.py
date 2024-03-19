"""Binary Search Tree
    in-order: left -> root -> right
    pre order: root -> left -> right
    post order: left -> right -> root

 """
import random

class BinarySearchTreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None # will hold a BinarySearchTreeNode()
        self.right = None # will hold a BinarySearchTreeNode()

    def insert(self, data):
        if data == self.data: # if the value we're adding already exists do nothing
            return

        if data < self.data: # if value is less than the current node, we'll add to the left sub tree
            if self.left: # the current node has a left child, we must now travel to it recursively
                self.left.insert(data) # we recursively travel to the next node implicitly through our check

            else: # we have found a leaf node
                self.left = BinarySearchTreeNode(data) # add a new node

        elif data > self.data: #if vallue is greater than current node, add a new node to the right sub tree
            if self.right: # current node has a child
                self.right.insert(data) #recursively travel to the right node

            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self): # in-order: left -> root -> right
        nodes = []

        # while we have left sub trees keep going to max depth
        if self.left:
            nodes+=self.left.in_order_traversal()

        # appending the root after left node(s)
        nodes.append(self.data)

        # perform the same depth search for the right sub tree
        if self.right:
            nodes+=self.right.in_order_traversal()

        return nodes

    def pre_order_traversal(self): # pre order: root -> left -> right
        nodes = []

        nodes.append(self.data)

        if self.left:
            nodes+=self.left.pre_order_traversal()

        if self.right:
            nodes+=self.right.pre_order_traversal()

        return nodes

    def post_order_traversal(self): # post order: left -> right -> root
        nodes = []

        if self.left:
           nodes+=self.left.post_order_traversal()

        if self.right:
            nodes+=self.right.post_order_traversal()

        nodes.append(self.data)

        return nodes

    def min(self):
        if self.left is None:
            return self.data
        return self.left.min()

    def max(self):
        if self.right is None:
            return self.data
        return self.right.max()


    def search(self, val):
        if self.data == val: # found item
            print("FOUND!")
            return True

        if val < self.data: # move left from current node
            if self.left:
                return self.left.search(val) # recurse and root is now the left node
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def delete(self, val):

        # recursively search the tree for our values
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)

        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)

        else: # we've found the node
            if self.left is None and self.right is None:
                return None # node has no children

            if self.left is None:
                return self.right # if the item we're removing has a right node return it to take the deleted node's place

            if self.right is None:
                return self.left # otherwise we do the left node

            #case: 2 children
            #find the min value of the right subtree
            min_val_r_sub_tree = self.right.in_order_traversal()[0]
            self.data = min_val_r_sub_tree
            self.right = self.right.delete(min_val_r_sub_tree) # deletes children of right subtree

        return self

# helper function to quickly create a tree
def build_tree(vals):
    root = BinarySearchTreeNode(vals[0])

    for i in range(len(vals)):
        root.insert(vals[i])

    return root

#merging 2 trees
def merge_trees(reciever_tree, donor_tree):

    # if a tree has a node in a position the other tree does not, this is the trivial case of just adding it
    if not reciever_tree:
        return donor_tree
    if not donor_tree:
        return reciever_tree

    #recursive merging
    reciever_tree.left = merge_trees(reciever_tree.left, donor_tree.left)
    reciever_tree.right = merge_trees(reciever_tree.right, donor_tree.right)

    return reciever_tree

def is_binary_search_tree(tree):
    # a binary traversal should have an ordered list of all elements, if this list is not ordered then the tree was not a bst
    if tree.in_order_traversal() != sorted(tree.in_order_traversal):
        return False
    return True


