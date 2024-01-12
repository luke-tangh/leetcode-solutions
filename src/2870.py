from collections import Counter

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        def getOp(n):
            if n % 3 == 0: return n // 3
            else: return n // 3 + 1
        
        count = Counter(nums)
        ret = 0

        for n in count.values():
            if n == 1: return -1
            ret += getOp(n)
        
        return ret
        