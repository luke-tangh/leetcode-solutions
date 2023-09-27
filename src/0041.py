class Solution:
    def firstMissingPositive(self, nums) -> int:
        nums = list(set(nums))
        nums.sort()
        i = 0
        k = nums[i]
        
        if len(nums) == 1:
            if nums[0] <= 0:
                return 1
            elif nums[0] > 1:
                return 1
            else:
                return 2
        
        while i < len(nums)-1 and k <= 0:
            i += 1
            k = nums[i]
            
        if nums[i] <= 0:
            return 1
        if k > 1:
            return 1
        
        while i < len(nums):
            if k != nums[i]:
                return k
            i += 1
            k += 1
        return k