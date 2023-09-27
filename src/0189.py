class Solution:
    def rotate(self, nums, k: int) -> None:
        n = len(nums)
        k = k % n
        nums[:] = nums[-k:] + nums[:-k]