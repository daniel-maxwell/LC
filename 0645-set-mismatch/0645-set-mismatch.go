func findErrorNums(nums []int) []int {
    n := len(nums)
    numSet := make(map[int]bool)
    var duplicate int
    var missing int

    for i := 1; i <= n; i++ {
        if _, present := numSet[nums[i-1]]; present {
            duplicate = nums[i-1]
        }
        numSet[nums[i-1]] = true
    }

    for n >= 1 {
        if _, present := numSet[n]; !present {
            missing = n
            break
        }
        n--
    }

    return []int{duplicate, missing}
}