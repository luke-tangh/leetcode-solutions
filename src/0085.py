class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        heights = [0 for i in range(len(matrix[0]))]
        ret = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "0":
                    heights[j] = 0
                else:
                    heights[j] += 1
            ret = max(ret, self.largestRectangleArea(heights))
        return ret
    
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
