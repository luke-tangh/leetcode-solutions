class Solution:
    def getLastMoment(self, n: int, left: list[int], right: list[int]) -> int:
        if not left:
            return n - min(right)
        elif not right:
            return max(left)
        else:
            return max(max(left), n - min(right))
