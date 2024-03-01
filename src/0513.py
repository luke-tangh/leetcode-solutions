# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        Q = [root]
        for n in Q:
            if n.right:
                Q += [n.right]
            if n.left:
                Q += [n.left]
        return n.val
