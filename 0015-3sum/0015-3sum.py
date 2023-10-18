class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:     
        counts, res, added = {}, [], set()
        for num in nums[1:]: counts[num] = 1 if num not in counts else counts[num] + 1
        countsCopy = counts.copy()
        
        i = 0

        while counts:
            j = i + 1
            while j < len(nums):
                if counts[nums[j]] > 1:
                    counts[nums[j]] -= 1
                else:
                    counts.pop(nums[j])

                lower = min(nums[i], nums[j])
                higher = max(nums[i], nums[j])
                target = -(lower + higher)

                if target in counts and (lower, higher) not in added:
                    res.append([lower, higher, target])
                    added.add((lower, higher))
                    added.add((min(lower, target), max(lower, target)))
                    added.add((min(higher, target), max(higher, target)))

                j += 1
            i += 1

            if countsCopy[nums[i]] > 1:
                countsCopy[nums[i]] -= 1
            else: countsCopy.pop(nums[i])
            counts = countsCopy.copy()

        return res