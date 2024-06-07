class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

        newImg = []

        for r in range(len(img)):
            newImg.append([])
            for c in range(len(img[r])):
                cells = [img[r][c]]
                for dr, dc in directions:
                    move = (r + dr, c + dc)
                    if (
                        move[0] < 0 or
                        move[0] == len(img) or
                        move[1] < 0 or
                        move[1] == len(img[0])
                    ):
                        continue

                    cells.append(img[move[0]][move[1]])
                
                avg = math.floor(sum(cells) / len(cells))
                newImg[r].append(avg)

        return newImg