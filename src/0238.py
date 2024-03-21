class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [1 for _ in range(n)]
        cur = 1
        for i in range(0, n):
            res[i] *= cur
            cur *= nums[i]
        cur = 1
        for i in range(n - 1, -1, -1):
            res[i] *= cur
            cur *= nums[i]
        return res
