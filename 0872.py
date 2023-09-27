# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        self.arr1 = []
        self.arr2 = []
        self.dfs(root1, 0)
        self.dfs(root2, 1)
        return self.arr1 == self.arr2

    def dfs(self, root, idx):
        if root.left:
            self.dfs(root.left, idx)
        if root.right:
            self.dfs(root.right, idx)
        if not (root.right or root.left):
            if idx == 0:
                self.arr1.append(root.val)
            else:
                self.arr2.append(root.val)
