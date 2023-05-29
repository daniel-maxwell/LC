/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    let j=0;
    for (let i=0; i<nums.length; i++) { 
        if (nums[j] === 0) {
            nums.push(0);
            nums.splice(j, 1);
            j--;
        }
        j++;
    }
    return nums
};