class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.s = s
        res = ""
        for i in range(len(s)):
            res = max(self.palindrome(i, i), self.palindrome(i, i+1), res, key=len)
        return res
        
    def palindrome(self, left, right):
        while left >= 0 and right < len(self.s) and self.s[left] == self.s[right]:
            left -= 1
            right += 1
        return self.s[left+1:right]
