class Solution:
    def runningSum(self, nums):
        temp = 0
        ret = []
        for i in range(len(nums)):
            temp += nums[i]
            ret.append(temp)
        return ret
                