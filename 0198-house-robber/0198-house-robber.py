class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        
        ''' for every element n in nums, 
        
        take the max between:
            > the element n + the maximum amount we could have accumelated so far if we exclude element n-1
            > the element n-1 + the maximum amount we could have accumelated so far if we exclude element n-2
        '''
        
        for n in nums:
            tmp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = tmp
        
        return rob2