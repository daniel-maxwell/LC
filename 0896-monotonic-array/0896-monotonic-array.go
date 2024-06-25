func isMonotonic(nums []int) bool {
    var dir int = 2
    for i := 1; i < len(nums); i++ {
        if nums[i] > nums[i-1] {
            if dir == 0 {
                return false
            } else {
                dir = 1
            }
        } else if nums[i] < nums[i-1] {
            if dir == 1 {
                return false
            } else {
                dir = 0
            }
        }
    }
    return true
}