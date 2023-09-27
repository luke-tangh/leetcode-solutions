from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        fcount = defaultdict(int)
        i = 0
        for j in range(len(fruits)):
            fcount[fruits[j]] += 1
            if len(fcount) > 2:
                fcount[fruits[i]] -= 1
                if fcount[fruits[i]] == 0:
                    del fcount[fruits[i]]
                i += 1
        return j-i+1
