class Solution {
    fun twoSum(nums: IntArray, target: Int): IntArray {
        val intMap = mutableMapOf<Int, Int>()
        nums.forEachIndexed { index, value -> 
            if (intMap.containsKey(target - value)) {
                return intArrayOf(intMap.getValue(target - value), index)
            }
            intMap[value] = index
        }
        throw IllegalArgumentException("No two sum solution")
    }
}