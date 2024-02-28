class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        def isPalindrome(word: str):
            n = len(word)
            l = r = n // 2
            if n % 2 == 0:
                l -= 1
            while l > -1 and r < n:
                if word[l] != word[r]:
                    return False
                l -= 1
                r += 1
            return True
        
        for w in words:
            if isPalindrome(w):
                return w
        
        return ""
