class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        if len(tokens) == 1:
            return 1 if tokens[0] <= power else 0

        tokens.sort()
        l = 0
        r = len(tokens) - 1
        scores = [0]
        score = 0
        
        while l < r:
            while tokens[l] <= power:
                power -= tokens[l]
                score += 1
                l += 1
            scores.append(score)
            if tokens[l] > power:
                power += tokens[r]
                score -= 1
                r -= 1
            if score < 0: break
        
        return max(scores)
