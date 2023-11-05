class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        def findPivot(nums):
            l, r, res = 0, len(nums)-1, -1
            mid = l + ((r - l) // 2)

            if nums[l] < nums[r]: return res

            while l <= r:
                if mid-1 >= 0 and nums[mid-1] > nums[mid]:
                    res = mid
                    break
                elif mid+1 < len(nums) and nums[mid] > nums[mid+1]:
                    res = mid + 1
                    break
                else:
                    if nums[mid] > nums[r] and nums[mid] > nums[l]:
                        l = mid + 1
                    elif nums[mid] < nums[l] and nums[mid] < nums[r]:
                        r = mid - 1
                mid = l + ((r - l) // 2)
            return res

        pivot = findPivot(nums)

        return nums[0] if pivot == -1 else nums[pivot]