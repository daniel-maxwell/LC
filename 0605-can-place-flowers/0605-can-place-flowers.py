class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0: return True
        if (len(flowerbed) == 1):
            return flowerbed[0] == 0 and n <= 1
        if n >= len(flowerbed): return False
        if (len(flowerbed) == 2):
            return sum(flowerbed[:]) < n
        if (len(flowerbed) == 3):
            return sum(flowerbed[:2]) < n or sum(flowerbed[1:]) < n

        availableSpaces = 0

        for i in range(1, len(flowerbed)-1):

            if i == 1:
                if flowerbed[i-1] + flowerbed[i] == 0:
                    flowerbed[i-1] = 1
                    availableSpaces += 1

            elif i == len(flowerbed)-2:
                if flowerbed[i] + flowerbed[i+1] == 0:
                    flowerbed[i+1] = 1
                    availableSpaces += 1

            elif flowerbed[i-1] + flowerbed[i] + flowerbed[i+1] == 0:
                flowerbed[i] = 1
                availableSpaces += 1

        return availableSpaces >= n