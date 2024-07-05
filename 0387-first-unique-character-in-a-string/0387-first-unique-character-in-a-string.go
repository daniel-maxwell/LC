func firstUniqChar(s string) int {
    stack := make(map[string]int)

    for i := 0; i < len(s); i++ {
        stack[string(s[i])]++
    }

    for i := 0; i < len(s); i++ {
        if stack[string(s[i])] == 1 {
            return i
        }
    }
    return -1
}