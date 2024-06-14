class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        def backtrack(i, curr):
            if i == len(nums):
                xorTotal = 0
                for num in curr:
                    xorTotal ^= num
                nonlocal res
                res += xorTotal
                return

            curr.append(nums[i])
            backtrack(i+1, curr)
            curr.pop()
            backtrack(i+1, curr)

        backtrack(0, [])
        return res