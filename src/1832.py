class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        chars = set()
        for c in sentence:
            chars.add(c)
        return True if len(chars) == 26 else False