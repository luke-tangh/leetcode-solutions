from copy import deepcopy

class Solution:
    def gameOfLife(self, board) -> None:
        """
        1 -> 0: neighbor < 2 or neighbor > 3
        1 -> 1: neighbor : 2 or 3
        0 -> 1: neighbor > 3
        """
        temp = deepcopy(board)
        ymax = len(board)
        xmax = len(board[0])
        for y in range(ymax):
            for x in range(xmax):
                block = temp[y][x]
                neighbor = 0
                if x > 0 and y > 0 and temp[y-1][x-1]:
                    neighbor += 1
                if y > 0 and temp[y-1][x]:
                    neighbor += 1
                if y > 0 and x+1 < xmax and temp[y-1][x+1]:
                    neighbor += 1
                if x > 0 and temp[y][x-1]:
                    neighbor += 1
                if x+1 < xmax and temp[y][x+1]:
                    neighbor += 1
                if y+1 < ymax and x > 0 and temp[y+1][x-1]:
                    neighbor += 1
                if y+1 < ymax and temp[y+1][x]:
                    neighbor += 1
                if y+1 < ymax and x+1 < xmax and temp[y+1][x+1]:
                    neighbor += 1
                if block:
                    if neighbor < 2 or neighbor > 3:
                        board[y][x] = 0
                else:
                    if neighbor == 3:
                        board[y][x] = 1

        print(board)

temp = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Solution().gameOfLife(temp)