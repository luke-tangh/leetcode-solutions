class Solution:
    def maximumWealth(self, accounts) -> int:
        curmax = 0
        for i in range(len(accounts)):
            cursum = 0
            for j in range(len(accounts[i])):
                cursum += accounts[i][j]
            curmax = max(curmax, cursum)
        return curmax