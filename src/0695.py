class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        self.maxarea = self.area = 0
        self.grid = grid
        self.height, self.length  = len(grid), len(grid[0])
        for x in range(self.length):
            for y in range(self.height):
                self.area = 0
                self.dfs(y, x)
                self.maxarea = max(self.maxarea, self.area)
        return self.maxarea
    
    def dfs(self, r, c):
        if self.grid[r][c] == 1:
            self.grid[r][c] = 0
            self.area += 1
            if r >= 1: #up
                self.dfs(r-1, c)
            if r + 1 < self.height: #down
                self.dfs(r+1, c)
            if c >= 1: #left
                self.dfs(r, c-1)
            if c + 1 < self.length: #right
                self.dfs(r, c+1)