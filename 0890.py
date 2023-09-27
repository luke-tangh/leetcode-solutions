class Solution:
    def findAndReplacePattern(self, words, pattern: str):
        return [n for n in words if len(set(n)) == len(set(zip(n,pattern))) == len(set(pattern))]