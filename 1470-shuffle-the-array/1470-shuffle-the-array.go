func shuffle(nums []int, n int) []int {
    var a, b = 0, n
    res := []int{}

    for {
        res = append(res, nums[a], nums[b])
        a++
        b++
        if b == len(nums) {
            break
        }
    }
    
    return res
}