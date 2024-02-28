class Solution:
    def targetIndices(self, nums, target: int):
        ret = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == target:
                ret.append(i)
            elif nums[i] > target:
                break
        return ret
    