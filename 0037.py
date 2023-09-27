class Solution:

    def solveSudoku(self, board) -> None:
        self.backtrack(board, 0, 0)
        print(board)
                    
    def backtrack(self, board, r: int, c: int) -> bool:
        while board[r][c] != '.':
            c += 1
            if c == 9:
                c, r = 0, r+1
            if r == 9:
                return True
        for k in range(1, 10):
            if self.isValidSudokuMove(board, r, c, str(k)):
                board[r][c] = str(k)
                if self.backtrack(board, r, c):
                    return True
        board[r][c] = '.'
        return False
    
    def isValidSudokuMove(self, board, r: int, c: int, cand: str) -> bool:
        if any(board[r][j] == cand for j in range(9)):
            return False
        if any(board[i][c] == cand for i in range(9)):
            return False
        br, bc = 3*(r//3), 3*(c//3)
        if any(board[i][j] == cand for i in range(br, br+3) for j in range(bc, bc+3)):
            return False
        return True

board = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
Solution().solveSudoku(board)
