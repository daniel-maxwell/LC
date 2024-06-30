func destCity(paths [][]string) string {
    outboundPaths := make(map[string]bool)

    for i := 0; i < len(paths); i++ {
        outboundPaths[paths[i][0]] = true
    }

    for i := 0; i < len(paths); i++ {
        _, present := outboundPaths[paths[i][1]]
        if present == false {
            return paths[i][1]
        }
    }
    return ""
}