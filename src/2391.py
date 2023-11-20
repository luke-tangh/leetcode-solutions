class Solution:
    def garbageCollection(self, garbage: list[str], travel: list[int]) -> int:
        ret = 0
        for c in "MPG":
            time = 0
            reach = 0
            for i in range(len(garbage)):
                cs = garbage[i].count(c)
                if cs > 0:
                    time += cs
                    reach = i
            time += sum(travel[:reach])
            ret += time
        return ret
