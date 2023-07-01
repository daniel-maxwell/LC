class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1: return nums
        mid = math.floor(len(nums)/2)
        return Solution.merge(self, Solution.sortArray(self, nums[0:mid]), Solution.sortArray(self, nums[mid:]))

    def merge(self, left, right):
        res = []
        while 0 < len(left) and 0 < len(right):
            if left[0] <= right[0]:
                res.append(left[0])
                del left[0]
            else:
                res.append(right[0])
                del right[0]
        if len(left) > 0:
            res = res + left
        else:
            res = res + right
        return res