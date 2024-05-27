class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        for r in range(1, len(triangle)):
            for i in range(len(triangle[r])):
                a = triangle[r-1][i-1] if i > 0 else float('inf')
                b = triangle[r-1][i] if i < len(triangle[r-1]) else float('inf')
                triangle[r][i] += min(a, b)
        
        print(triangle)
        return min(triangle[-1])