class Solution:
    def reverse(self, x: int) -> int:
        y = list(str(x))
        y.reverse()
        negative = False
        
        if y[-1] == "-":
            negative = True
            y.pop()

        MAX = (2**31) - 1
        MIN = (-2) ** 31
        total = int(y[0])

        for d in y[1:]:
            
            if (10 * total) + int(d) > MAX or (10 * total) + int(d) < MIN:
                return 0

            total = (10*total) + int(d)

        return total if not negative else -total
