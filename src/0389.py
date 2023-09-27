from collections import defaultdict

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        charcount = defaultdict(int)
        for n in s:
            charcount[n] += 1
        for n in t:
            charcount[n] -= 1
        for c in charcount.keys():
            if charcount[c]:
                return c