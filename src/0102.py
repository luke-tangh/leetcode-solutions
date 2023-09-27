# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left         
        self.right = right

class Solution:
    def levelOrder(self, root):
        res = []
        self.leveling(root, 0, res)
        return res
        
    def leveling(self, root, level, res):
        if root is None:
            return
        if len(res) <= level:
            res.append([])
        res[level].append(root.val)
        self.leveling(root.left, level + 1, res)
        self.leveling(root.right, level + 1, res)