class Solution:
    def lastStoneWeight(self, stones) -> int:
        while len(stones) > 1:
            stones.sort()
            wy = stones.pop()
            wx = stones.pop()
            if wy > wx:
                stones.append(wy - wx)
        if len(stones) == 1:
            return stones[0]
        else:
            return 0