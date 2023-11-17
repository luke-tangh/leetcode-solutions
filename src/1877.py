class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        nums.sort()
        maxPair = 0
        i = 0 
        j = len(nums) - 1
        while i < j:
            maxPair = max(nums[i] + nums[j], maxPair)
            i += 1
            j -= 1
        return maxPair
