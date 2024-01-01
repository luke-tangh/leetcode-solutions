from string import ascii_lowercase

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        longest = -1
        for c in ascii_lowercase:
            l = 0
            r = len(s) - 1
            while l < r:
                if s[l] == s[r] == c:
                    longest = max(longest, r - l - 1)
                    break
                if s[l] != c: l += 1
                if s[r] != c: r -= 1
        return longest
