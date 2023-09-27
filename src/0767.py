from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        output = ""
        last = ""
        chars = Counter(s)
        sorted_chars = sorted(chars.items(), key=lambda d:d[1])
        max_char = sorted_chars[-1][1]
        if max_char - 1 > len(s) - max_char:
            return output
        while len(sorted_chars) > 1:
            i = -1
            if last == sorted_chars[-1][0]:
                i = -2
            output += sorted_chars[i][0]
            last = sorted_chars[i][0]
            chars[sorted_chars[i][0]] -= 1
            if chars[sorted_chars[i][0]] == 0:
                chars.pop(sorted_chars[i][0])
                sorted_chars.pop(i)
            sorted_chars = sorted(chars.items(), key=lambda d:d[1])
        return output + sorted_chars[-1][0]
