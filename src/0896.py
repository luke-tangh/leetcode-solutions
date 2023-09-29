class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        def isDec(n):
            for i in range(len(n) - 1):
                if n[i] < n[i + 1]:
                    return False
            return True
        
        def isAsc(n):
            for i in range(len(n) - 1):
                if n[i] > n[i + 1]:
                    return False
            return True

        return isAsc(nums) or isDec(nums)
