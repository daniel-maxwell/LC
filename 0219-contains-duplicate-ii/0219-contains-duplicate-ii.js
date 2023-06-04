/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var containsNearbyDuplicate = function(nums, k) {
    for (let i=0; i<nums.length; i++) {
        for (let j=i+1; j<nums.length; j++) {
            if ((Math.abs(i-j)) > k) break;
            if (nums[i] === nums[j]) return true
        }
    }
    return false
}
