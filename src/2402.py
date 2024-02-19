import heapq

class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        count = [0] * n
        rooms = []
        empty = [r for r in range(n)]
        heapq.heapify(empty)

        for (start, end) in sorted(meetings):           
            while rooms and rooms[0][0] <= start:
                time, room = heapq.heappop(rooms)
                heapq.heappush(empty, room)
            if empty:
                room = heapq.heappop(empty)
                heapq.heappush(rooms, (end, room))
            else:
                time, room = heapq.heappop(rooms)
                heapq.heappush(rooms, (time + end - start, room))
            count[room] += 1
        
        return count.index(max(count))
