class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pres = dict()
        longest, lpointer = 0, 0
        for i in range(len(s)):
            if s[i] not in pres:
                longest = max(longest, i-lpointer+1)
            else:
                if pres[s[i]] < lpointer:
                    longest = max(longest, i-lpointer+1)
                else:
                    lpointer = pres[s[i]] + 1
            pres[s[i]] = i
        return longest
