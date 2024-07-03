func isPathCrossing(path string) bool {
    coords := make(map[string]bool)
    location := []int{0, 0}
    coords[fmt.Sprintf("(%d,%d)", location[0], location[1])] = true
    directions := [][]int{
        {-1, 0},
        {1, 0},
        {0, -1},
        {0, 1},
    }
    compassMapping := map[string]int{
        "N": 0,
        "S": 1,
        "E": 2,
        "W": 3,
    }
    for i := 0; i < len(path); i++ {
        location[0] += directions[compassMapping[string(path[i])]][0]
        location[1] += directions[compassMapping[string(path[i])]][1]
        serializedLocation := fmt.Sprintf("(%d,%d)", location[0], location[1])
        if _, present := coords[serializedLocation]; present == true {
            return true
        }
        coords[serializedLocation] = true
    }
    return false
}