""""Lab Exercises:
In continuation of Lab exercise 4 and 5
Exercise-1:
In continuation of Lab exercise 4 and 5, Develop a Binary Search Tree (BST) which can perform the
following functions:
 Insert a new student with unique PSU ID and student details using BST.
 Find a student using PSU ID.
 Print each student with all details.
Hint: you can store the student’s details as a list or dictionary as a node in the BST"""

"""Modifying the BinarySearchTree From CMPSC 462: The data attribute of the BST will now hold a dictionary
with student deatils
    - student_id
    - name 

__gr__, __lt__, __eq__ will return the student_id
"""
import random

class BinarySearchTreeNode():
    def __init__(self, data: dict):
        self.data = data
        self.left = None # will hold a BinarySearchTreeNode()
        self.right = None # will hold a BinarySearchTreeNode()


    def insert(self, data):
        if data["student_id"] == self.data["student_id"]: # if the value we're adding already exists do nothing
            return

        if data["student_id"] < self.data["student_id"]: # if value is less than the current node, we'll add to the left sub tree
            if self.left: # the current node has a left child, we must now travel to it recursively
                self.left.insert(data) # we recursively travel to the next node implicitly through our check

            else: # we have found a leaf node
                self.left = BinarySearchTreeNode(data) # add a new node

        elif data["student_id"] > self.data["student_id"]: #if vallue is greater than current node, add a new node to the right sub tree
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
        if self.data["student_id"] == val: # found item
            print("\nSearch Results: "+f"\nName: {str().join(self.data['name'])}\nStudent_Id: {str().join(self.data['student_id'])}")
            return True

        if val < self.data["student_id"]: # move left from current node
            if self.left:
                return self.left.search(val) # recurse and root is now the left node
            else:
                return False

        if val > self.data["student_id"]:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def delete(self, val):

        # recursively search the tree for our values
        if val < self.data["student_id"]:
            if self.left:
                self.left = self.left.delete(val)

        elif val > self.data["student_id"]:
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



# generating some students
student_names = [
"mark",
    "greg",
    "ashley",
    "bob",
    "maria",
    "tamara",
    "mariami",
    "joe",
    "razie",
    "ishti",
    "tim",
    "jim",
    "calvin",
    "mark",
    "coco",
    "taazkir",
    "syed",
    "tyler",
    "sven",
    "peter",
    "tucker",
    "phil",
    "zeber"
]

students = []
for i in range(20):
    student = dict()

    student["student_id"] = "9"+"".join([" ".join(str(i)) for i in random.sample(range(0,9),8)])
    student["name"] = "".join(random.sample(student_names, 1)).title()
    students.append(student)


# making sure ids are unique
ids = [s["student_id"] for s in students]
print(len(set(ids)))

# if ids are unique, assemble the tree
if len(set(ids)) == len(students):
    root = students[0]

    student_tree = BinarySearchTreeNode(root)

    # add students to tree (insert function will handle this)
    for s in students:
        student_tree.insert(s)

    # getting ordered list of student details
    ordered_students = student_tree.in_order_traversal()
    count = 1
    for s in ordered_students:
        print(count, s)
        count+=1

    # finding a specific student
    idx = random.randint(0,len(students))
    print("\nStudent to find: "+str(students[idx]))

    print(student_tree.search(students[idx]["student_id"]))