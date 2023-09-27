class Solution:
    def minimumTotal(self, triangle) -> int:
        ans = triangle[-1]
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                ans[j] = min(ans[j], ans[j+1]) + triangle[i][j]
        return triangle[-1][:][0]