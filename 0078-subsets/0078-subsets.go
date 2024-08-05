func subsets(nums []int) [][]int {
    result := [][]int{}
    var backtrack func(cur []int, idx int)

    backtrack = func(cur []int, idx int) {
        if idx == len(nums) {
            result = append(result, cur)
            return
        }
        backtrack(cur, idx+1)
        cur = append(cur, nums[idx])
        curCopy := make([]int, len(cur))
        copy(curCopy, cur)
        backtrack(curCopy, idx+1)        
    }
    backtrack([]int{}, 0)
    return result
}