class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        ret = 0
        while n > 0:
            ret ^= n
            n >>= 1
        return ret
        