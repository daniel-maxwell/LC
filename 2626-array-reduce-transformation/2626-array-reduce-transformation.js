/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    if (nums.length === 0) {
        return init
    }
    for (i=0; i<nums.length; i++) {
        init = fn(init, nums[i])
    }
    return init
};