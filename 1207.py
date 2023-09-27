from collections import defaultdict

class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        cdict = defaultdict(int)
        for n in arr:
            cdict[n] += 1
        return len(cdict.values()) == len(set(cdict.values()))
