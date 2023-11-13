from collections import defaultdict
import heapq

class Graph:
    def __init__(self, n: int, edges: list[list[int]]):
        self.N = n
        self.INF = 10**19
        adj_list = defaultdict(list)
        for u, v, wt in edges:
            adj_list[u].append((v, wt))
        self.adj_list = adj_list

    def addEdge(self, edge: list[int]) -> None:
        self.adj_list[edge[0]].append((edge[1], edge[2]))

    def shortestPath(self, node1: int, node2: int) -> int:
        h = []
        heapq.heappush(h, (0, node1))
        dist = [self.INF] * self.N
        dist[node1] = 0
        
        while len(h):
            d, u = heapq.heappop(h)
            if u == node2 : return d
            if dist[u] < d : continue
            for v, wt in self.adj_list[u]:
                if dist[v] > dist[u] + wt:
                    dist[v] = dist[u] + wt
                    heapq.heappush(h, (dist[v], v))
        return -1
    