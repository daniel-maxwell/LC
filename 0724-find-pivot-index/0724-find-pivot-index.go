func pivotIndex(nums []int) int {

    leftSum := 0
    rightSum := 0

    for _, num := range nums {
        rightSum += num
    }
    
    rightSum -= nums[0]

    if leftSum == rightSum {
        return 0
    }
    
    for i := 0; i < len(nums) - 1; i++ {
        rightSum -= nums[i+1]
        leftSum += nums[i]

        if leftSum == rightSum {
            return i + 1
        }
    }

    return -1
}