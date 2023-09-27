class Solution:
    def numIslands(self, grid) -> int:
        island = 0
        height, length  = len(grid), len(grid[0])
        def dfs(r, c):
            if grid[r][c] == "1":
                grid[r][c] = "0"
                if r >= 1: #up
                    dfs(r-1, c)
                if r + 1 < height: #down
                    dfs(r+1, c)
                if c >= 1: #left
                    dfs(r, c-1)
                if c + 1 < length: #right
                    dfs(r, c+1)
        for i in range(height):
            for j in range(length):
                if grid[i][j] == "1":
                    dfs(i, j)
                    island += 1
        return island