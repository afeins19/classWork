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
    def __init__(self, data, parent, l_child = None, r_child = None):
        self.data = data
        self.parent = parent
        self.l_child = l_child
        self.r_child = r_child

    def __eq__(self, other):
        return self.data == other.data

    def __gr__(self, other):
        return self.data > other.data

    def __lt__(self, other):
        return self.data < other.data

class bst:
    def __init__(self, head):
        self.head = head

    def insert(self, node: Node):
        temp = self.head

        # while we can find the next node...
        while temp:
            if node.data > temp.data: #if our node is larger than current node...
                if temp.r_child is None:    # insert here
                    temp.r_child = node # set node as child of temp
                    node.parent = temp # set temp as parent of node
                    break
                else:
                    temp = temp.r_child # otherwise set the current node to its right child


            elif node.data < temp.data: # node is less than temp data
                if temp.l_child is None:
                    temp.l_child = node # set node as child of temp
                    node.parent = temp # set temp as parent of node
                    break
                else:
                    temp = temp.l_child

    def inorder(self, node):
        """In-order traversal:
            base case:
                - node is none (leaf node)->then begin ascent

            recursive calls:
                - traverse left subtree
                - visit root node
                - traverse right subtree
        """

        # base case
        if not node:
            return

        self.inorder(node.l_child)  # Traverse the left subtree
        print(" -> " + str(node.data),end="")  # Visit the node
        self.inorder(node.r_child)  # Traverse the right

    def preorder(self, node):
        """similar to in order just changed order of traversal
         root -> l -> r
        """
        # base case
        if not node:
            return

        print(" -> " + str(node.data), end="")  # Visit the node
        self.inorder(node.l_child)  # Traverse the left subtree
        self.inorder(node.r_child)  # Traverse the right


    def postorder(self, node):
        """l -> r -> root"""
        # base case
        if not node:
            return

        self.inorder(node.l_child)  # Traverse the left subtree
        self.inorder(node.r_child)  # Traverse the right
        print(" -> " + str(node.data), end="")  # Visit the node

    def find(self, val):
        temp = self.head

        while temp:
            if val == temp.data:  # check if  value matches current node data
                return temp
            elif val > temp.data:  # if the value is greater, move to the right child
                temp = temp.r_child
            else:  # if the value is less, move to the left child
                temp = temp.l_child

        return None

    def remove(self, val):
        # find the node to be removed.
        node = self.find(val)

        # if node not found.
        if not node:
            print(f"value {val} not found in the tree.")
            return

        # case: node with two children.
        if node.l_child and node.r_child:
            successor = node.r_child
            while successor.l_child:
                successor = successor.l_child
            # copy successor's data to node.
            node.data = successor.data
            # set node to successor so we remove the successor next.
            node = successor

        # cases: leaf node or node with one child.
        child = node.l_child if node.l_child else node.r_child

        if node.parent:
            if node == node.parent.l_child:
                node.parent.l_child = child
            else:
                node.parent.r_child = child
            if child:
                child.parent = node.parent
        else:  # node is root.
            self.head = child
            if child:
                child.parent = None

        # clear node
        node = None


head = Node(3, None, None, None)
a = Node(2, None, None, None)
b = Node(4, None, None, None)
c = Node(11, None, None, None)
d = Node(14, None, None, None)

head.l_child = a
head.r_child = b
b.l_child = c
b.r_child = d
b.parent = head
print(head.data)

numtree = bst(head)
numtree.inorder(head)

numtree.remove(14)
print("\n")
numtree.remove(14)

"""Here we've shown the tree traversal then performed a removal. Notice that the second removal attempt fails (node has been removed)"""







