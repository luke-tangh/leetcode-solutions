class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        heights.append(0)
        S = [-1]
        ret = 0
        for i in range(len(heights)):
            while heights[i] < heights[S[-1]]:
                h = heights[S.pop()]
                w = i - S[-1] - 1
                ret = max(ret, h * w)
            S.append(i)
        return ret
