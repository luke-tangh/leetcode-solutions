from collections import defaultdict

class Solution:
    def numBusesToDestination(self, routes: list[list[int]], source: int, target: int) -> int:
        stopToRoute = defaultdict(set)
        
        for i, stops in enumerate(routes):
            for stop in stops: 
                stopToRoute[stop].add(i)
                
        bfs = [(source,0)]
        seenStops = {source}
        seenRoutes = set()
        
        for stop, count in bfs:
            if stop == target: 
                return count
            
            for routeIndex in stopToRoute[stop]:
                if routeIndex not in seenRoutes:
                    seenRoutes.add(routeIndex)
                    for next_stop in routes[routeIndex]:
                        if next_stop not in seenStops:
                            seenStops.add(next_stop)
                            bfs.append((next_stop, count + 1))
        return -1
