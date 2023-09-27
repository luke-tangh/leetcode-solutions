class Solution:
    def plusOne(self, digits):
        num = ""
        res = []
        for n in digits:
            num += str(n)
        num = str(int(num)+1)
        for i in range(len(num)):
            res.append(num[i])
        return res