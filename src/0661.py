from math import floor

class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
        smoothed = [[0 for _ in range(len(img[0]))] for _ in range(len(img))]
        for i in range(len(img)):
            for j in range(len(img[0])):
                terms = 0
                value = 0
                for dx, dy in dirs:
                    x = i + dx
                    y = j + dy
                    if x < 0 or x >= len(img):
                        continue
                    if y < 0 or y >= len(img[0]):
                        continue
                    terms += 1
                    value += img[x][y]
                smoothed[i][j] = floor(value / terms)
        return smoothed
    