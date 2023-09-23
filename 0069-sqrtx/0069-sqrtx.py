class Solution:
    def mySqrt(self, x: int) -> int:
        sqroot = x//2
        square, upper = sqroot*sqroot, (sqroot+1)*(sqroot+1)
        prevHigh, prevLow = x, 0

        while not (square <= x and upper > x):
            if square < x and square+1 < x:
                prevLow = sqroot
                sqroot = sqroot + max(1, (abs(sqroot - prevHigh) // 2))

            elif square > x and square+1 > x:
                prevHigh = sqroot
                sqroot = sqroot - max(1, (abs(prevLow - sqroot) // 2))

            else:
                sqroot += 1

            square = sqroot * sqroot
            upper = (sqroot+1) * (sqroot+1)

        return sqroot