# Find a Corresponding Node of a Binary Tree in a Clone of That Tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        res = {}
        self.helper(cloned, target, res)
        return res['result']

    def helper(self, cloned, target, res):
        if res['stop']:
            return
        if cloned:
            self.helper(cloned.left, target, res)
            if cloned.val == target.val:
                res['result'] = cloned
                res['stop'] = True
                return
            self.helper(cloned.right, target, res)
