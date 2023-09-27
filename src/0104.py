# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def __init__(self):
        self.imax = 0
    
    def maxDepth(self, root) -> int:
        return self.dfs(root, 0)
    
    def dfs(self, root, i):
        if root:
            i += 1
            self.imax = max(self.imax, i)
            self.dfs(root.left, i)
            self.dfs(root.right, i)
            return self.imax
        else:
            return self.imax