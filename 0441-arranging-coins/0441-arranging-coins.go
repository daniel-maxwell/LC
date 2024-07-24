func arrangeCoins(n int) int {
	steps, result := 1, 0
	for steps <= n {
		if n - steps >= 0 {
			result++
			n -= steps
		} else {
			break
		}
        steps++
	}
	return result
}