from collections import defaultdict

class Solution:
    def findDiagonalOrder(self, nums: list[list[int]]) -> list[int]:
        max_key = 0
        diag = defaultdict(list)
        for r in range(len(nums) - 1, -1, -1):
            for c in range(0, len(nums[r])):
                diag[r + c].append(nums[r][c])
                max_key = max(max_key, r + c)
        ret = []
        for k in range(max_key + 1):
            ret += diag[k]
        return ret
