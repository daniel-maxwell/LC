/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function(nums1, m, nums2, n) {
    let i = 0, j = 0;
    while (n > 0) {
        if (nums1[m-i-1] >= nums2[n-1]) {
            nums1[nums1.length-j-1] = nums1[m-i-1];
            nums1[m-i-1] = 0;
            j++;
            i++;

        } else {
            nums1[nums1.length-j-1] = nums2[n-1];
            n--;
            j++;
        }
    }
    return nums1
};