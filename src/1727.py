class Solution:
    def largestSubmatrix(self, matrix: list[list[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        h = [0 for i in range(n)]
        ret = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    h[j] = 0
                else:
                    h[j] += 1
            sh = sorted(h)
            for k in range(n):
                ret = max(ret, sh[k] * (n - k))
        return ret
