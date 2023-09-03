class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        mid = len(nums) // 2
        output = []
        i = 0

        while i < mid:
            output.append(nums[i])
            output.append(nums[i+mid])
            i +=1

        return output


        