class Solution:
    def isAcronym(self, words: list[str], s: str) -> bool:
        ls = list(s)
        if len(words) != len(ls):
            return False
        for i in range(len(words)):
            if ls[i] != words[i][0]:
                return False
        return True
