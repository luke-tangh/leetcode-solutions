# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTarget(self, root, k: int) -> bool:
        return self.find(root, set(), k)
    
    def find(self, node, nodes, k):
        if not node:
            return False
        complement = k - node.val
        if complement in nodes:
            return True
        nodes.add(node.val)
        return self.find(node.left, nodes, k) or self.find(node.right, nodes, k)