class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort()
        ret = -1
        cur = 0
        for n in nums:
            cur += n
            if cur > n * 2:
                ret = cur
        return ret
    