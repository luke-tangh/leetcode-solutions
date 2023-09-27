# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self.sum = 0
        self.h = high
        self.l = low
        self.dfs(root)
        return self.sum
    
    def dfs(self, root):
        if root:
            if root.val >= self.l and root.val <= self.h:
                self.sum += root.val
            self.dfs(root.left)
            self.dfs(root.right)
