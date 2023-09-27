class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        return sum(list(col) != sorted(col) for col in zip(*strs))
        