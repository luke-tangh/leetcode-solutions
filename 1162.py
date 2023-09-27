from collections import deque

class Solution:
    def maxDistance(self, grid: list[list[int]]) -> int:
        Q = deque()
        d = -1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    Q.append((i, j, 0))

        if len(Q) == len(grid) * len(grid[0]) or len(Q) == 0:
            return d
        
        while(len(Q)):
            i, j, d = Q.popleft()
            dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
            for x, y in dirs:
                if 0 <= i+x < len(grid[0]) and 0 <= j+y < len(grid):
                    if grid[i+x][j+y] == 0:
                        grid[i+x][j+y] = 1
                        Q.append((i+x, j+y, d+1))
        return d
        