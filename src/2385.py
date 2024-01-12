# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.dist = 0
    
    def dfs(self, root: TreeNode, start: int):
        if not root:
            return (False, 0)
        
        s1, d1 = self.dfs(root.left, start)
        s2, d2 = self.dfs(root.right, start)

        if root.val == start:
            self.dist = max(self.dist, max(d1, d2))
            return (True, 0)
        
        if s1:
            self.dist = max(self.dist, d1 + d2 + 1)
            return (True, d1 + 1)
        elif s2:
            self.dist = max(self.dist, d1 + d2 + 1)
            return (True, d2 + 1)
        
        return (False, max(d1, d2) + 1)

    def amountOfTime(self, root: TreeNode, start: int) -> int:
        self.dfs(root, start)
        return self.dist
