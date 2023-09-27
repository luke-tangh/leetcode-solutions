class Solution:
    def countHomogenous(self, s: str) -> int:
        prev = s[0]
        count = 1
        ret = 0
        for i in range(1, len(s)):
            if s[i] == prev:
                count += 1
            else:
                ret += int((1 + count) * count / 2)
                prev = s[i]
                count = 1
        return (ret + int((1 + count) * count / 2)) % (10**9 + 7)