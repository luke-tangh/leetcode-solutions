# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.count = 0

    def averageOfSubtree(self, root: TreeNode) -> int:
        self.traversal(root)
        return self.count

    def traversal(self, root: TreeNode) -> (int, int):
        # returns: (x, y) -> (sum of nodes, number of nodes)
        if root is None:
            return (0,0)
        
        left_tree = self.traversal(root.left)
        right_tree = self.traversal(root.right)

        nodes_sum = left_tree[0] + root.val + right_tree[0]
        nodes_count = left_tree[1] + 1 + right_tree[1]

        if nodes_count != 0 and nodes_sum // nodes_count == root.val:
            self.count += 1
        
        return (nodes_sum, nodes_count)
