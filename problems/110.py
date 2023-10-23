# Problem name: Balanced Binary Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getHeight(self, root: TreeNode, depth: int):
        if root:
            left = self.getHeight(root.left, depth + 1)
            right = self.getHeight(root.right, depth + 1)
            return max(left, right)
        return depth

    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        leftHeight = self.getHeight(root.left, 0)
        rightHeight = self.getHeight(root.right, 0)
        if abs(leftHeight - rightHeight) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
