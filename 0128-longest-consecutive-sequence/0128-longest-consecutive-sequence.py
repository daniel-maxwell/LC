class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet, minVal = set(), 10000000000

        for i in range(0, len(nums)):
            if nums[i] < minVal:
                minVal = nums[i]
            hashSet.add(nums[i])

        maxChainLength = 0
        currChainLength = 1

        while len(hashSet) > 0:
            startVal = next(iter(hashSet))
            currVal = startVal + 1

            while currVal in hashSet:
                currChainLength += 1
                hashSet.remove(currVal)
                currVal += 1

            currVal = startVal - 1
            
            while currVal in hashSet:
                currChainLength += 1
                hashSet.remove(currVal)
                currVal -= 1

            if currChainLength > maxChainLength:
                maxChainLength = currChainLength

            currChainLength = 1
            hashSet.remove(startVal)
        
        return maxChainLength