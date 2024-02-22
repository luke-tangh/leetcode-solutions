class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        relation = [0 for _ in range(n)]
        for r in trust:
            relation[r[1] - 1] += 1
            relation[r[0] - 1] = -n
        return relation.index(max(relation)) + 1 if max(relation) == n - 1 else -1
