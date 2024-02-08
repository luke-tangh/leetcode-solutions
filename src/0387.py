from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        charcount = Counter(s)
        for i in range(len(s)):
            if charcount[s[i]] == 1:
                return i
        return -1
