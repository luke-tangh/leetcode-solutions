class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ret = 0
        for i in range(n):
            num = start + 2 * i
            ret ^= num
        return ret