class Solution:
    def sortVowels(self, s: str) -> str:
        vols = []
        s = list(s)
        for c in s:
            if self.isVowel(c):
                vols.append(c)
        vols.sort(reverse=True)
        for i in range(len(s)):
            if self.isVowel(s[i]):
                s[i] = vols.pop()
        return ''.join(s)

    def isVowel(self, char):
        return char.lower() in 'aeiou'
