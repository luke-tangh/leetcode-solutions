from collections import defaultdict

class Solution:
    def topKFrequent(self, nums, k: int):
        numcount = defaultdict(int)
        for n in nums:
            numcount[n] += 1
        ret = sorted(numcount, key=lambda n: (-numcount[n], n))
        return ret[:k]