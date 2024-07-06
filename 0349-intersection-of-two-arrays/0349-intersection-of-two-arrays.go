func intersection(nums1 []int, nums2 []int) []int {

    map1 := make(map[int]bool)
    map2 := make(map[int]bool)

    for i := 0; i < len(nums1); i++ {
        map1[nums1[i]] = true
    }

    for i := 0; i < len(nums2); i++ {
        map2[nums2[i]] = true
    }

    result := []int{}

    for k := range map1 {
        if _, present := map2[k]; present == true {
            result = append(result, k)
        }
    }

    return result
}