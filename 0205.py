class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # check unique items and their mappings
        return len(set(s)) == len(set(zip(s,t))) == len(set(t))