class Solution:
    def lengthOfLastWord(self, s):
        s = s.strip()
        for i in range(-1,-len(s),-1):
            if s[i] == " ":
                return abs(i)-1
        return len(s)