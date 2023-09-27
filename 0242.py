from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ana = defaultdict(int)
        for n in s:
            ana[n] += 1
        for m in t:
            if m in ana:
                ana[m] -= 1
        if not any(ana.values()):
            return True
        else:
            return False