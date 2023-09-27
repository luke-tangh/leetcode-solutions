class Solution:
    def maxProfit(self, prices) -> int:
        maxpro, curpro = 0, 0
        for i in range(1,len(prices)):
            curpro = max(0, curpro + (prices[i] - prices[i-1]))
            maxpro = max(maxpro, curpro)
        return maxpro