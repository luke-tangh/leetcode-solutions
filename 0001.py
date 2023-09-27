class Solution:
    def twoSum(self, nums, target):
        intmap = dict()
        for i in range(len(nums)):
            n = nums[i]
            if (target - n) in intmap:
                return [intmap[target - n], i]
            else:
                intmap[n] = i
