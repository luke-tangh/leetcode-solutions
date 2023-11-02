# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.arr = []
    
    def findMode(self, root: TreeNode) -> list[int]:
        self.inOrder(root)
        maxi = max(set(self.arr), key=self.arr.count)
        maxn = self.arr.count(maxi)
        ans = []
        for n in set(self.arr):
            if self.arr.count(n) == maxn:
                ans.append(n)
        return ans

    def inOrder(self, root: TreeNode) -> list[int]:
        if root.left:
            self.inOrder(root.left)
        if root.right:
            self.inOrder(root.right)
        self.arr.append(root.val)
