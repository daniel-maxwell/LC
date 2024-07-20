func groupAnagrams(strs []string) [][]string {

	groups := make(map[string][]string)

	for i := range (len(strs)) {
		intBuffer := make([]int, len(strs[i]))

		for j := range strs[i] {
			intBuffer[j] = int(strs[i][j])
		}
		slices.Sort(intBuffer)

		byteBuffer := make([]byte, len(strs[i]))

		for k := range len(intBuffer) {
			byteBuffer[k] = byte(intBuffer[k])
		}

		groups[string(byteBuffer)] = append(groups[string(byteBuffer)], strs[i])
	}

	result := [][]string{}

	for _, v := range groups {
		result = append(result, v)
	}

	return result
}