class Solution:
    def maxSubArray(self, nums) -> int:
        if len(nums) == 1:
            return nums[0]
        maxpro = curpro = nums[0]
        for i in range(1, len(nums)):
            curpro = max(nums[i], curpro + nums[i])
            maxpro = max(maxpro, curpro)
        return maxpro