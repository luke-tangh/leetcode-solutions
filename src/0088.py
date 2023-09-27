class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        y = 0
        for i in range(m + n):
            if y < n and i < m + y:
                if nums1[i] >= nums2[y]:
                    nums1.insert(i, nums2[y])
                    y += 1
            elif y < n:
                nums1.insert(i, nums2[y])
                y += 1
        nums1[:] = nums1[:m+n]