# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.diameter = 0
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def maxLength(root: TreeNode):
            if not root: return 0
            
            left = maxLength(root.left)
            right = maxLength(root.right)
            self.diameter = max(left + right, self.diameter)

            return max(left, right) + 1

        maxLength(root)

        return self.diameter
