from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ana = defaultdict(int)
        for n in s:
            ana[n] += 1
        for m in t:
            ana[m] -= 1
        return not any(ana.values())
