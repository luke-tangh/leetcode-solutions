class Solution:
    def reverseWords(self, s: str) -> str:
        rev = word = ""
        for i in range(len(s)):
            if s[i] == " ":
                rev += word + " "
                word = ""
            else:
                word = s[i] + word       
        return rev + word