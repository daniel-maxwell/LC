class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        minPath = [[triangle[0][0]]]
        res = minPath[0][0]
        
        i = 1
        while i < len(triangle):
            row, minVal = [float('inf')] * len(triangle[i]), float('inf')

            j = 0
            while j < len(minPath[-1]):
                row[j] = min(row[j], minPath[-1][j] + triangle[i][j])
                row[j+1] = min(row[j+1], minPath[-1][j] + triangle[i][j+1])
                minVal = min([row[j], row[j+1], minVal])
                j += 1

            res = minVal
            minPath.pop()
            minPath.append(row)
            i += 1

        return res