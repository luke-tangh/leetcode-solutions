from collections import defaultdict

class Solution:
    def countNicePairs(self, nums: list[int]) -> int:
        def reverse(n):
            r = 0
            while n > 0:
                r *= 10
                r += n % 10
                n //= 10
            return r
        pairs = 0
        count = defaultdict(int)
        for i in range(len(nums)):
            nums[i] -= reverse(nums[i])
            pairs += count[nums[i]]
            count[nums[i]] += 1
        return pairs % (10**9 + 7)
