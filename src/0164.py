class Solution:
    def maximumGap(self, nums) -> int:
        if len(nums) < 2:
            return 0
        nums.sort()
        maxdif = 0
        for i in range(1,len(nums)):
            dif = abs(nums[i-1] - nums[i])
            maxdif = max(maxdif, dif)
        return maxdif