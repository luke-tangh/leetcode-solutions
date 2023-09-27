class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        set1 = set(nums1)
        set2 = set()
        for n in set(nums2):
            if n in set1:
                set1.remove(n)
            else:
                set2.add(n)
        return [list(set1), list(set2)]
