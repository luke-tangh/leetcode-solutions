from collections import Counter

class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        numdict = Counter(nums)
        k = max(numdict.values())
        numlist = list(numdict.elements())
        return [numlist[i::k] for i in range(k)]
    