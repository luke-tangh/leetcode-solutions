class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        elif n == 1:
            return True
        else:
            for p in 2,3,5:
                while n % p == 0:
                    n /= p
            return n == 1