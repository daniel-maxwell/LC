/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    let i=0;
    let j=1;
    while (i != nums.length -1)
        {
            while (j != nums.length)
            {
                if (nums[i] === nums[j]) return true
                j = j+1
            }
            i = i + 1
            j = i + 1
        }
    return false
}