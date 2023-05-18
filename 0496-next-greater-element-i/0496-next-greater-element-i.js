/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */

var nextGreaterElement = function(nums1, nums2) {
    for (let i=0; i<nums1.length; i++) {
        const element = nums1[i];
        for (const el of nums2.slice(nums2.indexOf(nums1[i]))) {
            if (el > nums1[i]) {
                nums1[i] = el;
                break;
            }
        }
        if (nums1[i] === element) nums1[i] = -1;
    }
    return nums1
};