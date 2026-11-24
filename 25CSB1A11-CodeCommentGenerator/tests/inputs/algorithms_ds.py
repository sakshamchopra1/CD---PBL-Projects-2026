"""
Algorithms and Data Structures Sample — Binary Search Tree.
Tests recursive control flow, classes, and missing docstrings.
"""

class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val: int) -> None:
        if not self.root:
            self.root = TreeNode(val)
            return
        curr = self.root
        while True:
            if val < curr.val:
                if not curr.left:
                    curr.left = TreeNode(val)
                    break
                curr = curr.left
            else:
                if not curr.right:
                    curr.right = TreeNode(val)
                    break
                curr = curr.right

    def inorder_traversal(self, node: TreeNode = None) -> list:
        if node is None:
            node = self.root
        res = []
        if node and node.left:
            res.extend(self.inorder_traversal(node.left))
        if node:
            res.append(node.val)
        if node and node.right:
            res.extend(self.inorder_traversal(node.right))
        return res
