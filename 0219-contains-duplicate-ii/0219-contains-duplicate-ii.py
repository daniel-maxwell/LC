class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False

        def meetsReqs(i, j):
            if abs(i - j) <= k:
                return True
            return False
        
        sortedNums = []

        for idx, num in enumerate(nums):
            sortedNums.append((num, idx))
        sortedNums.sort()

        l, r = 0, 1

        while l < len(nums) - 1:
            r = l + 1
            while r < len(nums) and sortedNums[l][0] == sortedNums[r][0]:
                if meetsReqs(sortedNums[l][1], sortedNums[r][1]):
                    return True
                r += 1
            l += 1

        return False