from collections import Counter

class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        def good(word: str, p):
            for w in word:
                p[w] -= 1
                if p[w] < 0:
                    return False
            return True
        pool = Counter(chars)
        ret = 0
        for w in words:
            if good(w, pool.copy()):
                ret += len(w)
        return ret
