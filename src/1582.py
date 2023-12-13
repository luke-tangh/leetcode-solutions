class Solution:
    def numSpecial(self, mat: list[list[int]]) -> int:
        ret = 0
        rows = list(map(sum, mat))
        cols = [0 for _ in range(len(mat[0]))]
        for c in range(len(mat[0])):
            for r in range(len(mat)):
                if mat[r][c] != 0:
                    cols[c] += 1
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 1 and rows[r] == 1 and cols[c] == 1:
                    ret += 1
        return ret
