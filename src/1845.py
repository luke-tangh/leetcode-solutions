from sortedcontainers import SortedList

class SeatManager:
    def __init__(self, n: int):
        self.L = SortedList([], key=neg)
        self.seats = 1

    def reserve(self) -> int:
        seat_num = 0
        if self.L:
            seat_num = self.L.pop()
        else:
            seat_num = self.seats
            self.seats += 1
        return seat_num
            

    def unreserve(self, seatNumber: int) -> None:
        self.L.add(seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
