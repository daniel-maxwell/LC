class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        maxFruits = 0

        for start in range(len(fruits)):
            if maxFruits > len(fruits) - start: break
            fruitA, fruitB = fruits[start], None
            collected = 1

            if start + 1 == len(fruits):
                maxFruits = max(collected, maxFruits)
                break

            i = start + 1

            while i < len(fruits) and fruitA == fruits[i]:
                collected += 1
                i += 1
            if i == len(fruits):
                maxFruits = max(collected, maxFruits)
                break

            fruitB = fruits[i]

            while i < len(fruits) and (fruitA == fruits[i] or fruitB == fruits[i]):
                collected += 1
                i += 1

            maxFruits = max(collected, maxFruits)

        return maxFruits  