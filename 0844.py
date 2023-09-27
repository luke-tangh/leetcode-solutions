class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.convert(s) == self.convert(t)
    def convert(self, code) -> str:
        ret = ""
        for c in code:
            if c == '#':
                if ret:
                    ret = ret[:-1]
            else:
                ret += c
        return ret