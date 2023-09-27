class Solution:
    def moveZeroes(self, nums) -> None:
        i = 0
        for _ in range(len(nums)):
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
            else:
                i += 1