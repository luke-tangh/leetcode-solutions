from collections import defaultdict

class Solution:
    def topKFrequent(self, words, k: int):
        wordcount = defaultdict(int)
        for w in words:
            wordcount[w] += 1
        ret = sorted(wordcount, key=lambda word: (-wordcount[word], word))
        return ret[:k]