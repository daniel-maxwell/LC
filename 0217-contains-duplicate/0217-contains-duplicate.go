func containsDuplicate(nums []int) bool {
    i := 0
    counts := make(map[int]int)
    for i < len(nums) {
        counts[nums[i]]++;
        if counts[nums[i]] > 1 {
            return true;
        }
        i++;
    }
    return false;
}