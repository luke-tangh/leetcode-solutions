class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        n = len(matrix)
        for i in range(1, n):
            for j in range(n):
                matrix[i][j] += min(matrix[i-1][k] for k in (j-1, j, j+1) if 0 <= k < n)
        return min(matrix[-1])
