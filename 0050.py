class Solution:
    def myPow(self, x, n):
        self.x = x
        self.n = n
        if x == 0:
            return 0
        if n == 0:
            r = 1
        else:
            r = Solution.magPow(self)
        return r
    
    def magPow(self):
        if self.n < 0:
            self.x = 1/self.x
        mag = 1
        acc = self.x
        bipow = format(abs(self.n), "b")
        for i in reversed(str(bipow)):
            if i == '1':
                mag *= acc
            acc *= acc
        return mag

ret = Solution().myPow(71,100)
print(ret)

# 3^13 = 3^(BINARY 1101) = 3^8 * 3^4 * 3