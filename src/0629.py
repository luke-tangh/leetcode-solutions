class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        max_inv = n * (n - 1) // 2
        if k > max_inv:
            return 0
        if k == 0 or k == max_inv:
            return 1
        
        MOD = 10 ** 9 + 7

        dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            dp[i][0] = 1

        dp[2][1] = 1

        for i in range(3, n + 1):
            max_inv = min(k, i * (i - 1) // 2)
            for j in range(1,  max_inv + 1):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j] 
                if j >= i:
                    dp[i][j] -= dp[i - 1][j - i]
                dp[i][j] = (dp[i][j] + MOD) % MOD
        
        return dp[n][k]
