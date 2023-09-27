from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        chars = Counter(s)
        ret = ""
        for k, v in sorted(chars.items(),key=lambda d: d[1], reverse=True):
            ret += k*v
        return ret
        