class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return not (n <= 0 or n & (n-1))