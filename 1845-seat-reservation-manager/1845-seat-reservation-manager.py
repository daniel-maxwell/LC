class SeatManager:

    def __init__(self, n: int):
        self.unreserved = [x for x in range(1, n+1)]
        heapq.heapify(self.unreserved)
        

    def reserve(self) -> int:
        seat = heapq.heappop(self.unreserved)
        return seat
        

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.unreserved, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)