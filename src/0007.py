class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2147483647
        if x > 0:
            ret = int(str(x)[::-1])
        elif x < 0:
            ret = int(str(x)[:0:-1]) * -1
        else:
            return 0
        if ret > INT_MAX or ret < -INT_MAX - 1:
            return 0
        return ret
