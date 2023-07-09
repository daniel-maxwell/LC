class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1: return nums

        valToFreq = {}
        freqToVal = {}
        
        for i in range(0, len(nums)):
            if valToFreq.get(nums[i]) == None:
                valToFreq[nums[i]] = 1

                if freqToVal.get(1) == None:
                    freqToVal[1] = {nums[i]}
                else:
                    freqToVal[1].add(nums[i])
            
            else:
                valToFreq[nums[i]] += 1
                if freqToVal.get(valToFreq[nums[i]]) == None:
                    freqToVal[valToFreq[nums[i]]] = {nums[i]}
                    freqToVal[valToFreq[nums[i]]-1].remove(nums[i])
                else:
                    freqToVal[valToFreq[nums[i]]].add(nums[i])
                    freqToVal[valToFreq[nums[i]]-1].remove(nums[i])
        output = []
        j = 0
        Max = max(freqToVal.keys())

        while len(output) < k:
            output += freqToVal[Max-j]
            j +=1

        return output
        
        