from collections import Counter

class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        arr = []
        nums = Counter(arr1)
        for n in arr2:
            arr += [n for i in range(nums[n])]
            del nums[n]
        for n in sorted(nums):
            arr += [n for i in range(nums[n])]
        return arr
