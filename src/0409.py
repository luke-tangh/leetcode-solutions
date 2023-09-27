class Solution:
    def longestPalindrome(self, s: str) -> int:
        exist = set()
        for i in s:
            if i in exist:
                exist.remove(i)
            else:
                exist.add(i)
        return len(s) - len(exist) + 1 if len(exist) > 0 else len(s)