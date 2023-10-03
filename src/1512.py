from collections import defaultdict

class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        count = defaultdict(int)
        pairs = 0
        for n in nums:
            pairs += count[n]
            count[n] += 1
        return pairs
