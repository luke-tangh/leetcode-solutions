class Solution:
    def isPalindrome(self, s: str) -> bool:
        sect = ""
        for n in s:
            if n.isalpha() or n.isnumeric():
                sect += n
        sect = sect.lower()
        for i in range(len(sect)//2):
            if sect[i] != sect[-(i+1)]:
                return False
        return True