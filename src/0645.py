class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n = len(nums)
        sumA = sum(nums)
        sumB = sum(set(nums))
        return [sumA - sumB, ((1 + n) * n // 2) - sumB]
