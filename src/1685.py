class Solution:
    def getSumAbsoluteDifferences(self, nums: list[int]) -> list[int]:
        ret = []
        left = 0
        right = sum(nums)
        for i in range(len(nums)):
            ret.append(i * nums[i] - left + right - (len(nums) - i) * nums[i])
            left += nums[i]
            right -= nums[i]
        return ret
