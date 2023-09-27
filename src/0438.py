from collections import defaultdict

class Solution:
    def findAnagrams(self, s: str, p: str):
        ana = defaultdict(int)
        ret = []
        plen = len(p)
        slen = len(s)
        if plen > slen:
            return []
        for n in p:
            ana[n] += 1
        for i in range(plen-1):
            if s[i] in ana:
                ana[s[i]] -= 1
        for i in range(-1, slen - plen + 1):
            if i > -1 and s[i] in ana:
                ana[s[i]] += 1
            if i + plen < slen and s[i+plen] in ana: 
                ana[s[i+plen]] -= 1
            if not any(ana.values()):
                ret.append(i+1)
        return ret