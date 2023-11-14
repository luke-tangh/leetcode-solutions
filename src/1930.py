from string import ascii_lowercase

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ret = 0
        for c in ascii_lowercase:
            lp = 0
            rp = len(s) - 1
            while lp < rp and not (s[lp] == s[rp] == c):
                if s[lp] != c:
                    lp += 1
                if s[rp] != c:
                    rp -= 1
            if s[lp] == s[rp] == c:
                ret += len(set(s[lp + 1:rp]))
        return ret
