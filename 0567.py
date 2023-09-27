from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        charcount = defaultdict(int)
        ls1 = len(s1)
        ls2 = len(s2)
        for c in s1:
            charcount[c] += 1
        for c in s2[:ls1]:
            charcount[c] -= 1
        if not any(charcount.values()):
            return True 
        for i in range(ls2 - ls1 + 1):
            tail = i + ls1
            if tail < ls2:
                charcount[s2[i]] += 1
                charcount[s2[tail]] -= 1
            if not any(charcount.values()):
                return True
        return False