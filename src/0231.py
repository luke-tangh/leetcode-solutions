class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return False if n <= 0 or n & (n-1) else True