class Solution:
    def reductionOperations(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        ret = 0
        prev = nums[0]
        for i in range(n):
            if nums[i] != prev:
                ret += n - i
                prev = nums[i]
        return ret
