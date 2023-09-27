class Solution:
    def prefixCount(self, words, pref: str) -> int:
        plen = len(pref)
        count = 0
        for w in words:
            if w[0:plen] == pref:
                count += 1
        return count