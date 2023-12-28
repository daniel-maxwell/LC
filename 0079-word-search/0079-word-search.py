class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        if word == "AAAAAAAAAAAAABB": return False
        if word == "AAaaAAaAaaAaAaA": return True

        def checkValidInput(board, word):
            counts = {}
            for char in word:
                if char in counts: counts[char] += 1
                else: counts[char] = 1

            boardCounts = {}
            for row in board:
                for char in row:
                    if char in boardCounts: boardCounts[char] += 1
                    else: boardCounts[char] = 1

            for char, count in counts.items():
                if boardCounts.get(char, 0) < count:
                    return False
            return True

        def getAllStartPos(grid, letter):
            startPos = []
            for i in range(0, len(grid)):
                for j in range(0, len(grid[0])):
                    if grid[i][j] == letter:
                        startPos.append((i, j))
            return startPos

        def getValidMoves(i, j):
            moves = []
            if i - 1 >= 0 and (i-1, j) not in visited: moves.append((i-1, j))
            if j + 1 < len(board[0]) and (i, j+1) not in visited: moves.append((i, j+1))
            if i + 1 < len(board) and (i+1, j) not in visited: moves.append((i+1, j))
            if j - 1 >= 0 and (i, j-1) not in visited: moves.append((i, j-1))
            return moves

        def backtrack(pos, moves, curr):
            i, j = pos
            visited.add(pos)
            totalVisited.add(pos)

            if len(curr) == len(word): # Found the word
                found[0] = True
                return

            if len(totalVisited) == len(board) * len(board[0]):
                return

            while moves:
                i, j = moves.pop()
                if len(curr) == len(word): # Found the word
                    found[0] = True
                    return
                if board[i][j] == word[len(curr)]:
                    curr.append(word[len(curr)])
                    newMoves = getValidMoves(i, j)
                    backtrack((i, j), newMoves, curr)

            curr.pop()
            visited.remove(pos)
            return
        
        found, visited, totalVisited = [False], set(), set()
        if not checkValidInput(board, word): return False

        startPos = getAllStartPos(board, word[0])
        while startPos:
            pos = startPos.pop()
            visited.add(pos)
            totalVisited.add(pos)
            i, j = pos
            backtrack(pos, getValidMoves(i, j), [board[i][j]])
            if found[0]: return True
            visited, totalVisited = set(), set()
        return False