class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        numZeros = 0
        prod = 1
        for num in nums:
            if num == 0:
                numZeros += 1
            else:
                prod *= num
          
        for num in nums:
            if num == 0:
                output.append(0) if numZeros > 1 else output.append(int(prod))   
            else:
                output.append(0) if numZeros > 0 else output.append(int(prod*(num**-1)))
                    
        return output