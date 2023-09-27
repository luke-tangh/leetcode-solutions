# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        def dfs(root: TreeNode):
            if root == None: return 0
            curSum = dfs(root.left) + dfs(root.right) + root.val
            self.ans = max(self.ans, curSum * (self.totalSum - curSum))
            return curSum
        
        self.ans, self.totalSum = 0, 0
        self.totalSum = dfs(root)
        dfs(root)
        return self.ans % (10**9 + 7)
