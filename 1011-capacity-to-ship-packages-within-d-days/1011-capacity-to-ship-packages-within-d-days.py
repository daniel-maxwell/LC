class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        res = None

        # Binary search: have left and right pointers initialized to lowest and highest values
        # In this case, lowest weight capacity must be 1 (can carry a weight of 1 per day)
        # Highest must be max of weights * len(weights) /// can this be optimised?
 
        def checkCapacity(weights, days, capacity):
            dailyCapacity = capacity
            
            for weight in weights:
                if weight > capacity: return False

                if weight > dailyCapacity:
                    days -= 1
                    if not days: return False
                    dailyCapacity = capacity
                    dailyCapacity -= weight

                else:
                    dailyCapacity -= weight

            return True

        l, r = 1, 500 * len(weights)

        mid = l + ((r-l)//2)

        while l <= r:

            if checkCapacity(weights, days, mid):
                res = mid
                r = mid - 1

            else:
                l = mid + 1

            mid = l + ((r-l)//2)

        return res