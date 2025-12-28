class Solution {
    fun searchInsert(nums: IntArray, target: Int): Int {

        var l = 0
        var r = nums.size - 1
        var m = l + ((r - l) / 2)
        
        while (l < r) {
            val curr = nums[m]
            if (curr > target) {
                r = m - 1
            } else if (curr < target) {
                l = m + 1
            } else {
                return m
            }
            m = l + ((r - l) / 2)
        }

        if (nums[m] < target) {
            return m + 1
        }

        return m
    }
}