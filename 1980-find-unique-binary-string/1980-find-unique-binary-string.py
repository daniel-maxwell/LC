class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        numSet, res = set(nums), ""

        def backtrack(curr, i):
            nonlocal res
            
            num = ''.join(curr)
            if num not in numSet:
                res = num
                return

            if res or i == len(curr):
                return

            curr[i] = "1"
            backtrack(curr, i+1)
            curr[i] = "0"
            backtrack(curr, i+1)

        backtrack(["0"]*len(nums), 0)

        return res
