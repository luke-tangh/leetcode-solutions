# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxAncestorDiff(self, node, lo=10**6, hi=0):
        if not node: 
            return hi - lo
        lo, hi = min(lo, node.val), max(hi, node.val)
        return max(
            self.maxAncestorDiff(node.left, lo, hi), 
            self.maxAncestorDiff(node.right, lo, hi)
        )
