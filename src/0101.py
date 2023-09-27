# Definition for a binary tree node.
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root) -> bool:
        if not root:
            return True
        dq = collections.deque([(root.left,root.right),])
        while dq:
            node1, node2 = dq.popleft()
            if not node1 and not node2:
                continue
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            dq.append((node1.left,node2.right))
            dq.append((node1.right,node2.left))
        return True