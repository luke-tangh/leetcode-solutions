class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = {}
        def roll(n: int, target: int):
            if target > k * n:
                dp[n, target] = 0
                return 0
            if n == 0:
                return target == 0
            if target < 0:
                return 0
            if (n, target) in dp:
                return dp[n, target]
            acc = 0
            for num in range(1, k + 1):
                acc += roll(n - 1, target - num)
            dp[n, target] = acc
            return acc
        return roll(n, target) % (10**9 + 7)
