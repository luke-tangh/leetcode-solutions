class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        ss = {1:[]}
        for n in sorted(nums):
            ss[n] = max((ss[d] for d in ss if n % d == 0), key=len) + [n]
        return max(ss.values(), key=len)
