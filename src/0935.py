class Solution:
    def knightDialer(self, n: int) -> int:
        n0 = n1 = n2 = n3 = n4 = n5 = n6 = n7 = n8 = n9 = 1
        for _ in range(n - 1):
            n0, n1, n2, n3, n4, n5, n6, n7, n8, n9 = \
            n4 + n6, n6 + n8, n7 + n9, n4 + n8, \
            n0 + n3 + n9, 0, n0 + n1 + n7, \
            n2 + n6, n1 + n3, n2 + n4
        return (n0 + n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9) % (10**9 + 7)
