from collections import Counter

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        C = Counter(s)
        ans = [C.pop(c, 0) * c for c in order]
        for k, v in C.items():
            ans.append(k * v)
        return "".join(ans)
