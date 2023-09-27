class Solution:
    def addSpaces(self, s: str, spaces) -> str:
        ret = ""
        i = n = 0
        slen = len(s)
        spaceslen = len(spaces)
        while i < slen:
            if n < spaceslen and i == spaces[n]:
                ret += " "
                ret += s[i]
                n += 1
            else:
                ret += s[i]
            i += 1
        return ret