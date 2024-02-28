from collections import defaultdict

class Solution:
    def isValidSudoku(self, board) -> bool:
        numcount = defaultdict(int)
        # row
        for i in range(9):
            numcount.clear()
            for j in range(9):
                if board[i][j] != '.':
                    numcount[board[i][j]] += 1
            if any(i >= 2 for i in numcount.values()):
                return False

        # column
        for i in range(9):
            numcount.clear()
            for j in range(9):
                if board[j][i] != '.':
                    numcount[board[j][i]] += 1
            if any(i >= 2 for i in numcount.values()):
                return False

        # box
        for x in range(0, 9, 3):
            for y in range(0, 9, 3):
                numcount.clear()
                for i in range(y, y+3):
                    for j in range(x, x+3):
                        if board[i][j] != '.':
                            numcount[board[i][j]] += 1
                if any(i >= 2 for i in numcount.values()):
                    return False
        
        return True
