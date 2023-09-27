from collections import defaultdict

class Solution:
    def intersect(self, nums1, nums2):
        numcount = defaultdict(int)
        ret = []
        for n in nums1:
            numcount[n] += 1
        for n in nums2:
            if numcount[n]:
                numcount[n] -= 1
                ret.append(n)
        return ret