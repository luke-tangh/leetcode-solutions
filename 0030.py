from collections import defaultdict

class Solution:
    def findSubstring(self, s: str, words):
        wordlen = len(words[0])
        wordcount = defaultdict(int)
        ret = []
        for w in words:
            for c in w:
                wordcount[c] += 1
        for c in s[0:wordlen*len(words)]:
            wordcount[c] -= 1
        for i in range(len(s) - wordlen*len(words) + 1):
            if not any(wordcount.values()):
                seg = s[i:i+wordlen*len(words)]
                temp = words[:]
                for j in range(0, wordlen*len(words), wordlen):
                    if seg[j:j+wordlen] in temp:
                        temp.remove(seg[j:j+wordlen])
                if len(temp) == 0:
                    ret.append(i)
            if i+wordlen*len(words) < len(s):
                wordcount[s[i]] += 1
                wordcount[s[i + wordlen*len(words)]] -= 1
        return ret
