from collections import defaultdict

class Solution:
    def sumOfUnique(self, nums) -> int:
        numcount = defaultdict(int)
        nsum = 0
        for n in nums:
            numcount[n] += 1
        for n in numcount.keys():
            if numcount[n] == 1:
                nsum += n
        return nsum