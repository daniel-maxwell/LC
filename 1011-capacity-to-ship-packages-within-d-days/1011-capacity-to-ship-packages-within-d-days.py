class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        maxWeight = max(weights) * len(weights)

        def canShip(capacity, days):
            timetaken = 0
            currCapacity = capacity

            for weight in weights:
                
                if timetaken >= days:
                    return False

                if weight > capacity:
                    return False

                elif weight > currCapacity:
                    currCapacity = capacity - weight
                    timetaken += 1

                else:
                    currCapacity -= weight

            return timetaken < days

        minCap = float('inf')
        
        l, r = 0, maxWeight

        while l <= r:
            mid = l + ((r-l)//2)

            if canShip(mid, days):

                minCap = min(mid, minCap)
                r = mid - 1
            else:

                l = mid + 1

        return minCap