from math import sqrt

class Solution:
    def pivotInteger(self, n: int) -> int:
        ans = (n * n + n) // 2
        sq = int(sqrt(ans))
        return int(sq) if sq * sq == ans else -1
    