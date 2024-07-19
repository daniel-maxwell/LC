func specialArray(nums []int) int {
    slices.Sort(nums)
    idx := 0
    for x := range(nums[len(nums) - 1] + 1) {
        for x > nums[idx] {
            idx++
        }
        if x == len(nums) - idx {
            return x
        }
    }
    return -1
}