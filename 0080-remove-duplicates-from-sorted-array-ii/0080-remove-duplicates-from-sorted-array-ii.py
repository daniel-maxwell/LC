class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        originalLength = len(nums)
        j = 0
        k = 0
        currElement = None

        while j < originalLength:

            if len(nums) < 3: return len(nums)

            currElement = nums[len(nums) - 1]

            if (currElement == nums[0] and currElement == nums[1]):
                nums.pop()
                j += 1
                continue

            else:
                nums.insert(0, currElement)
                nums.pop()
                j += 1
                k += 1

        return k