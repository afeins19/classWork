
class HuffmanTreeNode():

    def __init__(self, data=None, l_child=None, r_child=None, position=None):
        self.data = data
        self.l_child = l_child
        self.r_child = r_child
        self.position = position # if its 0 or 1 with respect to its parent

    def __str__(self):
        return f"{self.data}"
