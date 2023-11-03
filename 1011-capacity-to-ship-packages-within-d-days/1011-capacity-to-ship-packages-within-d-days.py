class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
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

        l, r, result = 1, 500 * len(weights), None
        mid = l + ((r-l)//2)

        while l <= r:

            if checkCapacity(weights, days, mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
            mid = l + ((r-l)//2)

        return res