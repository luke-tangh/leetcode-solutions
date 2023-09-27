class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        plus = 0
        muti = 1
        for i in str(n):
            plus += int(i)
            muti *= int(i)
        return muti - plus