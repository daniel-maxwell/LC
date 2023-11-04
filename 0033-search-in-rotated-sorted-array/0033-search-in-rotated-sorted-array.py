class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) < 3: return nums.index(target) if target in nums else -1

        def findPivot(nums):
            l, r, res = 0, len(nums) - 1, -1
            mid = l + ((r-l) // 2)
            if nums[l] < nums[r]: return res
            while l <= r:
                if mid + 1 < len(nums) and nums[mid] > nums[mid+1]:
                    return mid + 1
                if mid - 1 >= 0 and nums[mid-1] > nums[mid]:
                    return mid
                elif nums[mid] < nums[l]: r = mid - 1
                else: l = mid + 1
                mid = l + ((r-l)//2)
            return mid

        def findTarget(nums, l, r, target):
            mid = l + ((r-l)//2)
            res = -1
            while l <= r:
                print(nums[mid])
                val = nums[mid]
                if val == target:
                    res = mid
                    break
                elif val > target: r = mid - 1          
                else: l = mid + 1
                mid = l + ((r-l)//2)
            return res

        pivot = findPivot(nums)

        if pivot == -1:
            return findTarget(nums, 0, len(nums)-1, target)

        else:
            if nums[pivot] <= target and nums[-1] >= target:
                return findTarget(nums, pivot, len(nums)-1, target)
            else:
                return findTarget(nums, 0, pivot - 1, target)