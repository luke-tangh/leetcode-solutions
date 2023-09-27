from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        charcount = defaultdict(int)
        for c in s:
            charcount[c] += 1
        for i in range(len(s)):
            if charcount[s[i]] == 1:
                return i
        return -1