class Solution:
    def eliminateMaximum(self, dist: list[int], speed: list[int]) -> int:
        for i in range(len(dist)):
            if dist[i] % speed[i] == 0:
                dist[i] = (dist[i] // speed[i]) - 1
            else:
                dist[i] = dist[i] // speed[i]
        dist.sort()
        for i in range(len(dist)):
            if dist[i] < i:
                return i
        return len(dist)
