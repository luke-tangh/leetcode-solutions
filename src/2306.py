from collections import defaultdict

class Solution:
    def distinctNames(self, ideas: list[str]) -> int:
        names = defaultdict(set)
        count = 0
        for n in ideas:
            names[n[0]].add(hash(n[1:]))
        for ka, va in names.items():
            for kb, vb in names.items():
                if kb >= ka: continue
                same = len(va & vb)
                count += (len(va) - same) * (len(vb) - same)
        return count*2
        