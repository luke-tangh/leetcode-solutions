from collections import defaultdict

class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        numcount = defaultdict(int)
        for n in nums:
            if n % 2 == 0:
                numcount[n] += 1
        if len(numcount.keys()) == 0:
            return -1
        vmax = max(numcount.values())
        kmin = 10**5 + 1
        for k in numcount.keys():
            if numcount[k] == vmax and k < kmin:
                kmin = k
        return kmin