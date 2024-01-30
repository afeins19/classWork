# value generation
import random
import timeit
from prettytable import prettytable  # used for printing data in tabular format
from LinkedLists.SinglyLinkedList import linkedlist as ll



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

# generating 1000 integers between 1 and 1000
vals_list = [random.randint(1,1000) for i in range(10000)]

# generating a dictionary of the integers
vals_dict = {k : v for k,v in zip(vals_list, vals_list)}

# generating a linked list from the values
vals_ll = ll()
for val in vals_list:
    vals_ll.append(val)

# generating a bianry search tree
vals_bst = build_tree(vals_list)


# custom utility functions
def measureTime(fun, vals=None, run_count=1):
    if vals:
        return timeit.timeit(lambda: fun(vals), number=run_count)
    return timeit.timeit(lambda: fun(), number=run_count)

# order of times is list, dict, bst, ll
time_dict = {
    "print": [],
    "retrieve": [],
    "insert": [],
    "delete": []
}


    # Printing:
time_dict["print"] = [measureTime(print, vals_list),
                      measureTime(print, vals_dict),
                      measureTime(vals_bst.pre_order_traversal),
                      measureTime(vals_ll.traverse)]


    # Retrieval


# generating 5 unique random numbers
to_find = random.sample(vals_list, 5)

def findVal(iterable):
    return [i in iterable for i in to_find]

# Measure retrieval time
# measureTime(vals_list.index, vals=to_find[0])
time_dict["retrieve"] = [measureTime(findVal, vals=vals_list)/5,
                         measureTime(findVal, vals=vals_dict)/5,
                         sum([measureTime(vals_bst.search, vals=i) for i in to_find])/5,
                         sum([measureTime(vals_ll.find_node, vals=i) for i in to_find])/5]

    # removal (will remove random numbers generated in to_find)
# getting indecies for the values to pop from the list
time_dict["delete"] = [sum([measureTime(vals_list.remove, vals=i) for i in to_find])/5,
                       sum([measureTime(vals_dict.pop, vals=i) for i in to_find])/5,
                       sum([measureTime(vals_bst.delete, vals=i) for i in to_find])/5,
                       sum([measureTime(vals_ll.delete, vals=i) for i in to_find])/5]

time_dict["insert"] = [sum([measureTime(vals_list.append, vals=i) for i in to_find])/5,
                       sum([measureTime(vals_dict.update, vals={i:i}) for i in to_find])/5,
                       sum([measureTime(vals_bst.insert, vals=i) for i in to_find])/5,
                       sum([measureTime(vals_ll.append, vals=i) for i in to_find])/5]

# average time Table creation and populating
avg_time_tb = prettytable.PrettyTable()
avg_time_tb.title = "Average Times"
avg_time_tb.field_names = ["Op", "List", "Dict", "BST", "LL"]

# statistics table
ds_indicies = ["list", "dict", "bst", "ll"]
min_time_dict = {}

rank_table = prettytable.PrettyTable()
rank_table.title = "DS Sorted by Min Time"
rank_table.field_names = ["-", 1,2,3,4]


for k in list(time_dict.keys()):
    # adding rows to the table for each value in the dict for each operation
    row=[k]
    row.extend(time_dict[k])
    avg_time_tb.add_row(row)



for k in list(time_dict.keys()):
    # adding rows to the table for each value in the dict for each operation
    row = [k]
    vals = [ds_indicies[time_dict[k].index(val)] for val in sorted(time_dict[k])]
    row.extend(vals)

    rank_table.add_row(row)


#[ds_indicies[time_dict[k].index(val)] for val in sorted(time_dict[k])]
print(avg_time_tb)
print(rank_table)


