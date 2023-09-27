from collections import defaultdict

class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        loses = defaultdict(int)
        nol = []; onel = []
        for i in range(len(matches)):
            loses[matches[i][0]] += 0
            loses[matches[i][1]] += 1
        for k, v in loses.items():
            if v == 0:
                nol.append(k)
            elif v == 1:
                onel.append(k)
        return [sorted(nol), sorted(onel)]
