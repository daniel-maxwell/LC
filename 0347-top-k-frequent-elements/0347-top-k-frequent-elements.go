func topKFrequent(nums []int, k int) []int {

	counts := make(map[int]int)

	for _, val := range nums {
		counts[val]++
	}

	pairs := [][]int{}

	for key, val := range counts {
		pairs = append(pairs, []int{key, val})
	}

	slices.SortFunc(pairs, func(a, b []int) int {
		return cmp.Compare(b[1], a[1])
	})

	result := make([]int, k)

	for i := range result {
		result[i] = pairs[i][0]
	}

	return result
}