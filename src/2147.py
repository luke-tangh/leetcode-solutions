class Solution:
    def numberOfWays(self, corridor: str) -> int:
        s1, s2, s3 = 1, 0, 0
        for c in corridor:
            if c == 'S':
                s1, s2, s3 = 0, s1 + s3, s2
            else:
                s1, s2, s3 = s1 + s3, s2, s3
        return s3 % (10**9+7) 
