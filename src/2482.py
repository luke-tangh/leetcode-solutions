class Solution:
    def onesMinusZeros(self, grid: list[list[int]]) -> list[list[int]]:
        m = len(grid[0])
        n = len(grid)
        ret = [[0 for _ in range(m)] for _ in range(n)]
        rows = list(map(sum, grid))
        cols = [0 for _ in range(m)]
        for c in range(m):
            for r in range(n):
                if grid[r][c] != 0:
                    cols[c] += 1
        for r in range(n):
            for c in range(m):
                ret[r][c] = 2 * (rows[r] + cols[c]) - (n + m)
        return ret
