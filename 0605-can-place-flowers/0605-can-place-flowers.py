class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        if len(flowerbed) < 2:
            return n == 0 or sum(flowerbed) == 0 
        
        for i in range(len(flowerbed)):
            if i == 0:
                if flowerbed[i] + flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    n -= 1

            elif i == len(flowerbed) -1:
                if flowerbed[i-1] + flowerbed[i] == 0:
                    n -= 1
                    flowerbed[i] = 1


            elif flowerbed[i-1] + flowerbed[i] + flowerbed[i+1] == 0:
                n -= 1
                flowerbed[i] = 1

        return n <= 0