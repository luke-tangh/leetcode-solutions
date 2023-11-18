class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        nums.sort()
        i = j = 0
        for _ in range(len(nums) - 1):
            if k < 0:
                k = k + (nums[j] - nums[i]) - (j - i) * (nums[j + 1] - nums[j])
                i += 1
                j += 1
            else:
                j += 1
                k -= (j - i) * (nums[j] - nums[j - 1])
        return j - i if k < 0 else j - i + 1
