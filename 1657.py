from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        w1 = Counter(word1)
        w2 = Counter(word2)
        if sorted(list(w1.values())) != sorted(list(w2.values())):
            return False
        if set(w1.keys()) != set(w2.keys()):
            return False
        return True
