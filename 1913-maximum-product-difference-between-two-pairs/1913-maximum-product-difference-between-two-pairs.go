func maxProductDifference(nums []int) int {
    slices.Sort(nums)
    return (nums[len(nums)-1] * nums[len(nums)-2]) - (nums[0] * nums[1])
}