class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        mid = l + (r-l) // 2

        while l < r:
            first = -1

            if mid == 0:                        # First element
                if nums[mid + 1] != nums[mid]:
                    return nums[mid]

            elif mid == len(nums) - 1:          # Last element
                if nums[mid - 1] != nums[mid]: 
                    return nums[mid]
                else:
                    first = mid - 1

            else:                               # Middle
                if nums[mid - 1] == nums[mid]:
                    first = mid - 1

                elif nums[mid + 1] != nums[mid]:
                    return nums[mid]

            if first == -1: first = mid

            if first % 2 == 0: l = mid + 1
            else: r = first - 1

            if l == r: return nums[l]

            mid = l + ((r-l) // 2)

        return nums[mid]