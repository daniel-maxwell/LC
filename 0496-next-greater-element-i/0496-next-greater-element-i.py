class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        for i in range(0, len(nums1)):  
            for j in range(0, len(nums2)):
                if nums1[i] == nums2[j]:
                    for k in range(j+1, len(nums2)):
                        if nums2[j] < nums2[k]:
                            nums1[i] = nums2[k]
                            break
                    break             
            if nums1[i] == nums2[j]: nums1[i] = -1 
        return nums1
                           
        