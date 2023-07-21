class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        negSq = [i**2 for i in nums if i < 0]
        nums = nums[len(negSq):]

        if len(nums) > 0:
            i = 0
            nums[i] **= 2
            
            while len(negSq) > 0 and nums[i] > negSq[-1]:
                nums = nums[:i] + [negSq.pop()] + nums[i:]
                i += 1
                
            while i < len(nums) - 1:
                j = i + 1
                nums[j] **= 2

                while len(negSq) > 0 and negSq[-1] <= nums[j]:
                    nums = nums[:j] + [negSq.pop()] + nums[j:]
                    i += 1
                    j += 1
                i += 1

            if len(negSq) > 0:
                negSq.reverse()
                nums = nums + negSq

        else:
            negSq.reverse()
            return negSq
        
        return nums