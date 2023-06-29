class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        set2 = set()
        intersection = set()
        for i in range(len(nums2)):
            if nums2[i] not in nums1:
                if nums2[i] not in intersection:
                    set2.add(nums2[i])
            else: 
                nums1.remove(nums2[i])
                intersection.add(nums2[i])
        return [list(nums1), list(set2)]