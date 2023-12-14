class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, curr, nums):
            i -= 1
            if i < 0:
                res.append(curr.copy())
                return

            # Going left (add)
            curr.append(nums[i])
            dfs(i, curr, nums)
             
            # Going right (stay same)
            curr.pop()
            dfs(i, curr, nums)

        while nums:
            curr = [nums[-1]]
            i = len(nums) - 1
            dfs(i, curr, nums)
            nums.pop()

        res.append([])
        return res