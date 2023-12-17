class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        added = set()
        res = []

        def dfs(i, curr, nums):
            i -= 1
            if i < 0:
                serialized = curr.copy()
                serialized.sort()
                serialized = str(serialized)
                if serialized in added:
                    return
                else:   
                    res.append(curr.copy())
                    added.add(serialized)
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