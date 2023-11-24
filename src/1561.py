class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        piles.sort()
        ret = 0
        left = len(piles) // 3
        for i in range(left, len(piles), 2):
            ret += piles[i]
        return ret
