from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if set(word1) != set(word2):
            return False
        w1 = Counter(word1)
        w2 = Counter(word2)
        if sorted(w1.values()) != sorted(w2.values()):
            return False
        return True
 