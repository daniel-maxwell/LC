func sortArrayByParity(nums []int) []int {

    swapLeft := func(nums []int, startIdx int, destIdx int) []int {
        temp := nums[startIdx]
        nums[startIdx] = nums[destIdx]
        nums[destIdx] = temp
        return nums
    }

    for i := 0; i < len(nums); i++ {
        if nums[i] % 2 == 0 {
            continue
        }

        j := i + 1
        for j < len(nums) && nums[j] % 2 != 0 {
            j++
        }
        if j == len(nums) {
            continue
        }

        nums = swapLeft(nums, j, i)
    }

    return nums
}