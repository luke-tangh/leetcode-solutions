class Solution:
    def maxLength(self, arr: list[str]) -> int:
        dp = [set()]
        for s in arr:
            if len(set(s)) != len(s):
                continue
            ss = set(s)
            for char_set in dp[:]:
                if char_set & ss:
                    continue
                dp.append(char_set | ss)
        return max(len(cs) for cs in dp)
