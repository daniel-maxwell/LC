class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def canEatAllBananas(speed):
            kokoLoc = 0
            timeRemaining = h

            while kokoLoc < len(piles) and timeRemaining > 0:
                pile = piles[kokoLoc]
                timeRemaining -= ceil(pile / speed)

                if timeRemaining >= 0:
                    kokoLoc += 1
                else:
                    break

            return kokoLoc == len(piles)

        l, r = 1, max(piles)
        minSpeed = r

        while l <= r:
            mid = l + ((r-l)//2)

            if canEatAllBananas(mid):
                r = mid - 1
                minSpeed = min(mid, minSpeed)

            else:
                l = mid + 1

        return minSpeed