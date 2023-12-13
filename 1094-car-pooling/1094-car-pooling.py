class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda trip:trip[1], reverse=True)
        capacityHeap , currCapacity, distTravelled = [], capacity, 0

        while trips:
            trip = trips.pop()
            distTravelled = trip[1]

            while capacityHeap and distTravelled >= capacityHeap[0][0]:
                currCapacity += heapq.heappop(capacityHeap)[1]

            currCapacity -= trip[0]
            if currCapacity < 0: return False
            
            heapq.heappush(capacityHeap, [trip[2], trip[0]])
        
        return True