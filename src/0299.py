from collections import defaultdict

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        countchar = defaultdict(int)
        bull = cow = 0
        for c in secret:
            countchar[c] += 1
        for i in range(len(secret)):
            s = secret[i]
            g = guess[i]
            if s == g:
                if countchar[g] == 0:
                    cow -= 1
                else:
                    countchar[g] -= 1
                bull += 1
            elif g in countchar and countchar[g] > 0:
                    countchar[g] -= 1
                    cow += 1
        return "{}A{}B".format(bull, cow)

s = "11231"
g = "01111"
print(Solution().getHint(s, g))