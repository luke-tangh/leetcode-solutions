class Solution:
    def romanToInt(self, s: str) -> int:
        n = 0
        trans = {
                'I' : 1,
                'V' : 5,
                'X' : 10,
                'L' : 50,
                'C' : 100,
                'D' : 500,
                'M' : 1000
                }
        for c in reversed(s):
            if n >= 5 and c == 'I':
                n -= trans[c]
            elif n >= 50 and c == 'X':
                n -= trans[c]
            elif n >= 500 and c == 'C':
                n -= trans[c]
            else:
                n += trans[c]
        return n
