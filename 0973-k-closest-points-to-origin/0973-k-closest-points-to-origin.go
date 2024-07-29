func kClosest(points [][]int, k int) [][]int {
    var calcDist func(x int, y int) float64

    calcDist = func(x int, y int) float64 {
        xFloat := float64(x)
        yFloat := float64(y)
        return math.Sqrt(math.Pow(xFloat, 2) + math.Pow(yFloat, 2))
    }

    distances := [][]float64{}

    for idx, coords := range points {
        dist := calcDist(coords[0], coords[1])
        distances = append(distances, []float64{dist, float64(idx)})
    }

    sort.Slice(distances, func(i, j int) bool {
		return distances[i][0] < distances[j][0]
	})

    result := [][]int{}

    for i := 0; i < k; i++ {
        result = append(result, points[int(distances[i][1])])
    }

    return result
}