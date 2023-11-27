# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        def traverse(root, depth):
            if root.left and root.right:
                return min(
                    traverse(root.left, depth + 1),
                    traverse(root.right, depth + 1)
                    )
            elif root.left:
                return traverse(root.left, depth + 1)
            elif root.right:
                return traverse(root.right, depth + 1)
            else:
                return depth
        
        if not root:
            return 0
        
        return traverse(root, 1)
