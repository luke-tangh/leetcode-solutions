class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        costs = [float('inf')] * n
        costs[src] = 0

        for _ in range(k + 1):
            copy = costs[:]
            for s, d, w in flights:
                copy[d] = min(copy[d], costs[s] + w)
            costs = copy
        
        return -1 if costs[dst] == float('inf') else costs[dst]
