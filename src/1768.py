class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        bound = min(len(word1), len(word2))
        merged = ""
        for i in range(bound):
            merged += word1[i] + word2[i]
        if bound == len(word1):
            return merged + word2[bound:]
        else:
            return merged + word1[bound:]
