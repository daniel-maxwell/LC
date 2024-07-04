func makeEqual(words []string) bool {
    charCounts := make(map[string]int)

    for i := range len(words) {
        for j := range len(words[i]) {
            charCounts[string(words[i][j])]++
        }
    }

    for _, v := range charCounts {
        if v % len(words) != 0 {
            return false
        }
    }
    return true
}