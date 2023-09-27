class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return True if n > 0 and (not n & (n-1) and n % 3 == 1) else False