class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        temp = 101
        p = 0
        for n in nums:
            if temp == n:
                continue
            else:
                nums[p] = n
                p += 1
            temp = n
        return p
