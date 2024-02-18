class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        res, mapping = [], {}
        maxEl = nums2[-1]

        for i in range(len(nums2)-1, -1, -1):
            if nums2[i] >= maxEl:
                maxEl = nums2[i]
                mapping[nums2[i]] = -1

            else:
                j = i
                while j < len(nums2) and nums2[j] <= nums2[i]:
                    j += 1
                if j == len(nums2):
                    mapping[nums2[i]] = -1
                else:
                    mapping[nums2[i]] = nums2[j] 

        for el in nums1:
            res.append(mapping[el])

        return res