class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()

        while len(stones) > 2:

            if stones[-1] == stones[-2]:
                stones.pop()
                stones.pop()

            else:
                brokenStone = stones.pop()
                stones[-1] = brokenStone - stones[-1]
                i = 1
                while i + 1 <= len(stones) and stones[-i] < stones[-(i+1)]:
                    stones[-i], stones[-(i+1)] = stones[-(i+1)], stones[-i] # swap
                    i += 1

        if len(stones) > 1:
            return max(stones[-1], stones[-2]) - min(stones[-1], stones[-2])
        else:
            return stones[0]