class Solution:
    def makeGood(self, s: str) -> str:
        modified = True
        while modified:
            s, modified = self.eleminate(s)
        return s
    
    def eleminate(self, s):
        letters = list(s)
        modified = False
        i = 1
        while i < len(letters):
            if abs(ord(letters[i-1])-ord(letters[i])) == 32:
                letters[i-1] = letters[i] = ""
                modified = True
                i += 1
            i += 1
        return "".join(letters), modified
        