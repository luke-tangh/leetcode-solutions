class Solution:
    def floodFill(self, image, sr: int, sc: int, color: int):
        height, length  = len(image), len(image[0])
        setcolor = image[sr][sc]
        if setcolor == color:
            return image
        def dfs(r, c):
            if image[r][c] == setcolor:
                image[r][c] = color
                if r >= 1: #up
                    dfs(r-1, c)
                if r + 1 < height: #down
                    dfs(r+1, c)
                if c >= 1: #left
                    dfs(r, c-1)
                if c + 1 < length: #right
                    dfs(r, c+1)
        dfs(sr, sc)
        return image