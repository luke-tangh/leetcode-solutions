class Solution:
    def isPathCrossing(self, path: str) -> bool:
        dirs = {'N': (0, 1), 'S': (0, -1), 'W': (-1, 0), 'E': (1, 0)}
        visited = set()
        visited.add((0, 0))
        x = y = 0
        for p in path:
            x += dirs[p][0]
            y += dirs[p][1]
            if (x, y) in visited:
                return True
            visited.add((x, y))
        return False
