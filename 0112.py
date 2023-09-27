# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.target = 0
        self.found = False
    
    def hasPathSum(self, root, targetSum: int) -> bool:
        self.target = targetSum
        self.dfs(root, 0)
        return self.found
    
    def dfs(self, root, psum):
        if root:
            psum += root.val
            if psum == self.target and (not root.left and not root.right):
                self.found = True
            else:
                self.dfs(root.left, psum)
                self.dfs(root.right, psum)