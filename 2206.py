from collections import defaultdict

class Solution:
    def divideArray(self, nums) -> bool:
        numcount = defaultdict(int)
        for n in nums:
            numcount[n] += 1
        return all(i % 2 == 0 for i in numcount.values())