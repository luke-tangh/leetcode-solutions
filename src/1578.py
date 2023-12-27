class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        ret = 0
        last = colors[0]
        sliced = [neededTime[0]]

        for i in range(1, len(colors)):
            if colors[i] == last:
                sliced.append(neededTime[i])
                continue
            
            if len(sliced) > 1:
                ret += sum(sorted(sliced)[:-1])

            sliced = [neededTime[i]]
            last = colors[i]
        
        if len(sliced) > 1:
            ret += sum(sorted(sliced)[:-1])
        
        return ret
