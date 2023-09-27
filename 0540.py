class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        n = 0
        for i in nums:
            n ^= i
        return n
