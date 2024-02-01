class Solution:
    def divideArray(self, nums: list[int], k: int) -> list[list[int]]:
        nums.sort()
        ret = []
        for i in range(0, len(nums), 3):
            if nums[i + 1] - nums[i] > k or nums[i + 2] - nums[i] > k:
                return []
            ret.append([nums[i], nums[i + 1], nums[i + 2]])
        return ret
