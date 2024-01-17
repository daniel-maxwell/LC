class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        visited = set() # will track all nodes already visited

        def isValidCoordinate(tup):
            if tup in visited: return False
            if (0 <= tup[0] < len(grid) and 0 <= tup[1] < len(grid[0]) and
                grid[tup[0]][tup[1]] == 0):
                return True
            else:
                return False
        
        def bfs():
            if not isValidCoordinate((0, 0)): return -1
            ROWS = len(grid)
            COLS = len(grid[0])
            q = deque() # a queue of nodes to visit
            length = 1 # length of the current path
            moves = [(1, 1), (1, 0), (0, 1), (0, 1), (1, -1), (-1, 1), (-1, 0), (0, -1), (-1, -1)]

            visited.add((0, 0)) # Add first coordinate to visited nodes
            q.appendleft((0, 0)) # Add first coordinate to queue

            while q:
                for _ in range(len(q)):
                    currNode = q.pop()
                    print(f"currNode: {currNode} | currLength: {length}")
                    if currNode == (ROWS-1, COLS-1):
                        return length
                    
                    for rDiff, cDiff in moves:
                        coordinate = (currNode[0] + rDiff, currNode[1] + cDiff)   
                        if not isValidCoordinate(coordinate): continue       
                        q.appendleft(coordinate)
                        visited.add(coordinate)
                length += 1

            return -1

        return bfs()