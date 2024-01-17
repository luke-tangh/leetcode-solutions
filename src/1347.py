from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        steps = 0
        ss = Counter(s)
        ts = Counter(t)
        for k in ss.keys():
            steps += max(0, ss[k] - ts[k])
        return steps
