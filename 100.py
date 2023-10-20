# Problem name: Same Tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        res = {'result': True}
        self.helper(p, q, res)
        return res['result']

    def helper(self, p: TreeNode, q: TreeNode, res: dict):
        if (not p and q) or (not q and p):
            res['result'] = False
            return
        if not p or not q:
            return
        if p.val != q.val:
            res['result'] = False
            return
        self.helper(p.left, q.left, res)
        self.helper(p.right, q.right, res)
