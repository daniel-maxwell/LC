/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var minimumDifference = function(nums, k) {
    if (nums.length < 2 || k === 1) return 0;

    nums = nums.sort((a, b) => {return a - b});
    let minDifference = Infinity;

    for (let i=0; i<=nums.length - k; i++) {
        const slice = nums.slice(i, i+k);
        let low = Infinity;
        let high = 0;

        for (const num of slice) {
            if (num < low) low = num;
            if (num > high) high = num;
        }
        if (high-low < minDifference) minDifference = high-low;
    }
    return minDifference 
};