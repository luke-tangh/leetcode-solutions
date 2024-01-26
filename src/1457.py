# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        def traverse(root, path):
            if not root:
                return 0
            
            if root.val in path:
                path.remove(root.val)
            else:
                path.add(root.val)

            if not root.left and not root.right:
                return 1 if len(path) <= 1 else 0
            
            return traverse(root.left, path.copy()) + traverse(root.right, path.copy())
        return traverse(root, set())
