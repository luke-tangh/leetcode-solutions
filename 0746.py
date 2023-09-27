class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        cur = 0
        lower = cost[0]
        if len(cost) >= 2:
            higher = cost[1]
        for i in range(2, len(cost)):
            cur = cost[i] + min(lower,higher)
            lower = higher
            higher = cur
            print(cur, lower, higher)
        return min(lower,higher)
    
    '''
    [1,100,1,1,1,100,1]
    
    cur = 1 + 1 = 2
    lower = 100
    higher = 2
    
    cur = 1 + 2 = 3
    lower = 2
    higher = 3
    
    cur = 1 + 2 = 3
    lower = 3
    higher = 3
    
    cur = 100 + 3 = 103
    lower = 3
    higher = 103
    
    cur = 1 + 3 = 4
    lower = 103
    higher = 4
    
    return 4
    '''