from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = max_count = 0
        count = defaultdict(int)
        for i in range(len(s)):
            count[s[i]] += 1
            max_count = max(max_count, count[s[i]])
            if max_length < k + max_count:
                max_length += 1
            else:
                count[s[i-max_length]] -= 1
        return max_length

s = "AABABBA"
k = 1
print(Solution().characterReplacement(s,k))

'''
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charcount = defaultdict(int)
        slen = len(s)
        p = i = maxlen = 0
        
        while i != slen:
            charcount[s[i]] += 1
            maxchar = max(charcount.values())
            charsum = sum(charcount.values())
            dif = charsum - maxchar
            if dif <= k:
                maxlen += 1
                i += 1
            else:
                charcount[s[i]] -= 1
                charsum -= 1
                break

        while slen - p > maxlen:
            if dif <= k:
                charcount[s[p+maxlen]] += 1
                maxchar = max(charcount.values())
                if dif <= k:
                    maxlen += 1
                    charsum += 1
            else:
                charcount[s[p]] -= 1
                charcount[s[p+maxlen]] += 1
                maxchar = max(charcount.values())
                p += 1
        return maxlen'''