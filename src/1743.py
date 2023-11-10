from collections import defaultdict

class Solution:
    def restoreArray(self, adjacentPairs: list[list[int]]) -> list[int]:
        ps = defaultdict(list)
        for a, b in adjacentPairs:
            ps[a].append(b)
            ps[b].append(a)
        res = []
        for k, v in ps.items():
            if len(v) == 1:
                res.append(k)
                res.append(v[0])
                break
        while len(res) < len(adjacentPairs) + 1:
            tail = res[-1]
            prev = res[-2]
            if ps[tail][0] != prev:
                res.append(ps[tail][0])
            else:
                res.append(ps[tail][1])
        return res
