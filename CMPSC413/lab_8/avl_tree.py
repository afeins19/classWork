# node
class Node:
    def __init__(self, val, l_child,r_child, h):
        self.val = val
        self.l_child = l_child
        self.r_child = r_child
        self.h = h


    def __str__(self):
        left_val = self.l_child.val if self.l_child else None
        right_val = self.r_child.val if self.r_child else None
        return f"{self.val} | left: {left_val} | right: {right_val}"

    def __lt__(self, other):
        return self.val < other.val

    def __gt__(self, other):
        return self.val > other.val

    def __eq__(self, other):
        return self.val == other.val

