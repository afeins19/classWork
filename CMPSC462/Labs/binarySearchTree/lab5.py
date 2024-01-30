class BinarySearchTreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None # will hold a BinarySearchTreeNode()
        self.right = None # will hold a BinarySearchTreeNode()

    def insert(self, data):
        if data == self.data:  # if the value we're adding already exists do nothing
            return

    def insert(self, data):
        if data == self.data:  # if the value we're adding already exists do nothing
            return

        if data < self.data:
            self.left.insert(data)

        else:
            self.left = BinarySearchTreeNode(data)

        elif data > self.data:
            if self.right:  # current node has a child
                self.right.insert(data)

            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):  # in-order: left -> root -> right
        nodes = []

        # while we have left sub trees keep going to max depth
        if self.left:
            nodes += self.left.in_order_traversal()

        # appending the root after left node(s)
        nodes.append(self.data)
        # perform the same depth search for the right sub tree
        if self.right:
            nodes += self.right.in_order_traversal()
        return nodes

    def pre_order_traversal(self):  # pre order: root -> left -> right
        nodes = []

        nodes.append(self.data)
        if self.left:
            nodes += self.left.pre_order_traversal()
        if self.right:
            nodes += self.right.pre_order_traversal()
        return nodes

    def post_order_traversal(self):  # post order: left -> right -> root
        nodes = []

        if self.left:
            nodes += self.left.post_order_traversal()
        if self.right:
            nodes += self.right.post_order_traversal()
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
        if self.data == val:  # found item
            print("FOUND!")
            return True

        if val < self.data:  # move left from current node

            if self.left:
                return self.left.search(val)  # recurse and root is now the left node
            else:
                return False
        if val > self.data:
            if self.right:
                return self.right.search(val)
        else:
            return False
