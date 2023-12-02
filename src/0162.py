class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        nums = [-2 ** 32] + nums + [-2 ** 32]
        for i in range(1, len(nums) - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                return i - 1
        return -1
