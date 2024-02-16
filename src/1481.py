from collections import Counter

class Solution:
    def findLeastNumOfUniqueInts(self, arr: list[int], k: int) -> int:
        nums = Counter(arr)
        removed = 0
        for n in sorted(nums.values()):
            if k >= n:
                k -= n
                removed += 1
        return len(nums) - removed
    