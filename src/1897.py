from collections import defaultdict

class Solution:
    def makeEqual(self, words: list[str]) -> bool:
        charcount = defaultdict(int)
        for s in words:
            for c in s:
                charcount[c] += 1
        return all(n % len(words) == 0 for n in charcount.values())
