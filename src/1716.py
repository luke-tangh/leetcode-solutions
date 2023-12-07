class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        last = n % 7
        return (49 + weeks * 7) * weeks // 2 + (2 * weeks + last + 1) * last // 2
