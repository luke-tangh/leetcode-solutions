from functools import cache

class Solution:
    def minDifficulty(self, jobDifficulty: list[int], d: int) -> int:
        @cache
        def f(i, d):
            n = len(jobDifficulty)
            if i == n or d == 0:
                if i == n and d == 0: return 0
                else: return float("inf")
            
            result = float("inf")
            dayDiff = 0

            for j in range(i, n - d + 1):
                dayDiff = max(dayDiff, jobDifficulty[j])
                result = min(result, dayDiff + f(j + 1, d - 1))

            return result
        
        result = f(0, d)
        return -1 if result == float("inf") else result
    