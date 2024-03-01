from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        Q = deque([(root, 0)])
        cur = -1

        while len(Q) > 0:
            node, level = Q.popleft()
            if cur < level:
                cur = level
                prev = 0 if level % 2 == 0 else 10**6 + 1

            if node.val % 2 != (level + 1) % 2: return False
            if level % 2 == 0 and node.val <= prev: return False
            if level % 2 == 1 and node.val >= prev: return False
            
            prev = node.val

            if node.left:
                Q.append((node.left, level + 1))
            if node.right:
                Q.append((node.right, level + 1))

        return True
