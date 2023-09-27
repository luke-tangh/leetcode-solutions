from collections import deque

class Solution:
    def updateMatrix(self, mat):
        q = deque()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    mat[i][j] = -1

        while q:
            x, y = q.popleft()
            for r, c in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                newX, newY = x+r, y+c
                if 0 <= newX < len(mat) and 0 <= newY < len(mat[0]) and mat[newX][newY] == -1:
                    mat[newX][newY] = mat[x][y] + 1
                    q.append((newX, newY))
        return mat