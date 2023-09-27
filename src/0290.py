class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        k = pattern
        t = s.split()
        return len(set(zip(k, t))) == len(set(k)) == len(set(t)) and len(k) == len(t)