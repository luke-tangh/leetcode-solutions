import heapq

class Solution:
    def furthestBuilding(self, heights: list[int], bricks: int, ladders: int) -> int:
        skips = []
        for i in range(len(heights) - 1):
            gap = heights[i + 1] - heights[i]
            if gap > 0:
                heapq.heappush(skips, gap)
            if len(skips) > ladders:
                bricks -= heapq.heappop(skips)
            if bricks < 0:
                return i
        return len(heights) - 1
