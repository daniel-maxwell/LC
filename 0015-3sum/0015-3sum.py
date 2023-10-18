class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        aSet, res = set(), []

        for a in range(0, len(nums)-2):
            
            if nums[a] in aSet:
                a += 1
                continue

            lSet, rSet, = set(), set()
            l, r = a + 1, len(nums)-1

            while l < r:
                summed = nums[a] + nums[l] + nums[r]

                if summed == 0:
                    res.append([nums[a], nums[l], nums[r]])
                    lSet.add(nums[l])
                    rSet.add(nums[r])

                elif summed < 0:
                    lSet.add(nums[l])
                    l += 1
                else:
                    rSet.add(nums[r])
                    r -= 1

                
                while nums[l] in lSet and l < r: l += 1
                while nums[r] in rSet and r > l: r -= 1

            aSet.add(nums[a])
            a += 1

        return res