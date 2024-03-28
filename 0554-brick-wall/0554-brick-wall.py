class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        gaps, maxGaps = {}, 0

        for row in wall:
            col = 0
            for brick in row[:-1]:
                col += brick
                if col in gaps:
                    gaps[col] += 1
                else:
                    gaps[col] = 1

                maxGaps = max(maxGaps, gaps[col])

        return len(wall) - maxGaps