func numIdenticalPairs(nums []int) int {
    slices.Sort(nums)
    numEls := 1
    res := 0

    for i := 1; i < len(nums); i++ {
        if nums[i] == nums[i-1] {
            numEls++
        } else {
            if numEls == 1 {
                continue
            }
            res += numEls * (numEls - 1) / 2
            numEls = 1
        }
    }

    if numEls != 1 {
        res += numEls * (numEls - 1) / 2
    }

    return res
}