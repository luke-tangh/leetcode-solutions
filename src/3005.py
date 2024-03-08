from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        C = Counter(nums)
        max_val = max(C.values())
        return sum([x for x in C.values() if x == max_val])
