from functools import reduce

class Solution:
    def superPow(self, a: int, b: list[int]) -> int:
        return 0 if a % 1337 == 0 else pow(a, reduce(lambda x, y: (x * 10 + y) % 1140, b) + 1140, 1337)