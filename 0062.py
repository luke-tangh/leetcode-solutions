import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        pascal_row = m+n-2
        dp = [1]
        while pascal_row > 0:
            temp = []
            for i in range(1,len(dp)):
                temp.append(dp[i] + dp[i-1])
            dp = [1] + temp + [1]
            pascal_row -= 1        
        return dp[n-1]