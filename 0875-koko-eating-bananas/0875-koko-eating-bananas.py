class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles): return max(piles)
        if len(piles) == 1: return math.ceil(piles[0]/h)
        piles.sort()

        l, r = max(1, len(piles)//h), math.ceil((len(piles) * piles[-1]) / h)
        lowest = max(piles[-1], r)
        speed = l + ((r-l) // 2)
        speeds = []

        while l <= r:
            speeds.append(speed)
            hourCount = 0
            i = len(piles)-1

            while i >= 0 and speed < piles[i] and hourCount < h:
                hourCount += math.ceil(piles[i] / speed)
                i -= 1
            hourCount += i + 1
        
            if hourCount <= h:
                if speed < lowest: lowest = speed
                r = speed - 1
                
            else:
                l = speed + 1

                
            speed = l + ((r-l) // 2)

        return int(lowest)