class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        mod = 10 ** 9 + 7

        def search(m, n, move, row, col, dp):
            if move < 0: return 0
            if row >= m or col >= n or row < 0 or col < 0: return 1
            if dp[row][col][move] != -1: return dp[row][col][move] % mod

            ans = 0
            l = search(m, n, move - 1, row, col - 1, dp) % mod
            r = search(m, n, move - 1, row, col + 1, dp) % mod
            u = search(m, n, move - 1, row + 1, col, dp) % mod
            d = search(m, n, move - 1, row - 1, col, dp) % mod

            ans = (l + r + u + d) % mod
            dp[row][col][move] = ans
            return ans
        
        dp = [[[-1 for _ in range(maxMove + 1)] for _ in range(n + 1)] for _ in range(m + 1)]
        return search(m, n, maxMove, startRow, startColumn, dp) % mod
