
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:

        def inorderTraversal(root):
            # in order traversal...creates a list representation of tree
            if root:
                return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)
            return []  # empty case

        sorted_values = inorderTraversal(root)

        def build(lst):
            if not lst:
                return None

            mid = len(lst) // 2
            node = TreeNode(lst[mid])

            node.left = build(lst[:mid])

            node.right = build(lst[mid + 1:])

            return node

        return build(sorted_values)

