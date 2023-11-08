class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx == fx and sy == fy:
            return t != 1
        else:
            diff = min(abs(fx - sx), abs(fy - sy))
            line = abs(fx - sx) + abs(fy - sy) - 2*diff
            return line + diff <= t
