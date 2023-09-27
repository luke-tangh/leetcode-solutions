from collections import defaultdict

class Solution:
    def missingNumber(self, nums) -> int:
        numcount = defaultdict(bool)
        for n in nums:
            numcount[n] = True
        for i in range(len(nums) + 1):
            if not numcount[i]:
                return i