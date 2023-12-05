class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ret = ""
        for i in range(2, len(num)):
            if num[i - 2] == num[i - 1] == num[i]:
                ret = max(ret, num[i]*3)
        return ret
