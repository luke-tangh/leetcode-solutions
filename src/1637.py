class Solution:
    def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
        xs = [xy[0] for xy in points]
        xs.sort()
        diff = 0
        for i in range(1, len(xs) - 1):
            diff = max(diff, xs[i] - xs[i - 1])
        return diff
