class Solution:
    def balancedStringSplit(self, s: str) -> int:
        rcount = lcount = scount = 0
        for c in s:
            if c == 'L':
                lcount += 1
            elif c == 'R':
                rcount += 1
            if rcount == lcount:
                rcount = lcount = 0
                scount += 1
        return scount