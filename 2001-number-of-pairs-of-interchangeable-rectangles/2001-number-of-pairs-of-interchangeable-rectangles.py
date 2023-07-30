class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        ratios = {}
        numInterchangable = 0

        for i in range(0, len(rectangles)):
            ratio = rectangles[i][0] / rectangles[i][1]
            if ratio not in ratios:
                ratios[ratio] = 1
            else: ratios[ratio] += 1

        
        for count in ratios.values():
            if count > 1:
                p = math.factorial(count) / math.factorial(count - 2)
                numInterchangable += (p / 2)

        return int(numInterchangable)