class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        ret = 0
        for i in range(len(points) - 1):
            x1, y1 = points[i][0], points[i][1]
            x2, y2 = points[i + 1][0], points[i + 1][1]
            ret += max(abs(x1 - x2), abs(y1 - y2))
        return ret
