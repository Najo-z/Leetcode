# Problem name: Symmetric Tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.res = []

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        left = self.getDFS(root.left)
        self.res = []
        right = self.getDFS(root.right)
        left.reverse()
        return left == right

    def getDFS(self, root: TreeNode):
        if root:
            self.getDFS(root.left)
            self.res.append(root.val)
            self.getDFS(root.right)
        return self.res
