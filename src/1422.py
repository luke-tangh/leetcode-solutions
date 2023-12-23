class Solution:
    def maxScore(self, s: str) -> int:
        ret = 0
        l = 0
        r = s.count('1')
        for c in s[:-1]:
            if c == '1':
                r -= 1
            else:
                l += 1
            ret = max(ret, l + r)
        return ret
