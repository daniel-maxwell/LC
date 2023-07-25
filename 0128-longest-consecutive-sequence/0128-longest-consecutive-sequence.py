class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet, maxChain, currChain = set(nums), 0, 1

        while len(hashSet) > 0:
            startVal = next(iter(hashSet))
            currVal = startVal + 1

            while currVal in hashSet:
                currChain += 1
                hashSet.remove(currVal)
                currVal += 1

            currVal = startVal - 1
            
            while currVal in hashSet:
                currChain += 1
                hashSet.remove(currVal)
                currVal -= 1

            if currChain > maxChain:
                maxChain = currChain

            currChain = 1
            hashSet.remove(startVal)

        return maxChain