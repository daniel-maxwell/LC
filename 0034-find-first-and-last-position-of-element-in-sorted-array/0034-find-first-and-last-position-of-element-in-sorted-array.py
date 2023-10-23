class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r, res = 0, len(nums)-1, [-1, -1]

        while l <= r:
            m = l + ((r-l)//2)

            if nums[m] > target:
                r = m - 1

            elif nums[m] < target:
                l = m + 1

            else:
                l, r = m - 1, m + 1
                while l >= 0 and nums[l] == target: l -= 1
                while r < len(nums) and nums[r] == target: r += 1
                res = [l+1, r-1]
                break

        return res