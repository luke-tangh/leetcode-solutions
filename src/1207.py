from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        cdict = Counter(arr)
        return len(cdict.values()) == len(set(cdict.values()))
