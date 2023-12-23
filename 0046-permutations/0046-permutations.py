class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def swap(nums, a, b):
            nums[a], nums[b] = nums[b], nums[a]
            return nums

        def dfs(nums, leftPos):
            if leftPos == len(nums) - 1:
                res.append(nums.copy())

            else:
                for i in range(leftPos, len(nums)):
                    swap(nums, leftPos, i)
                    dfs(nums, leftPos + 1)
                    swap(nums, leftPos, i)

        dfs(nums, 0)

        return res