func minOperations(s string) int {
    currChar := []byte{'0', '1'}
    diffA := 0
    diffB := 0
    
    for i := 0; i < len(s); i++ {
        if s[i] == currChar[i % 2] {
            diffB++
        } else {
            diffA++
        }
    }

    if diffA < diffB {
        return diffA
    } else {
        return diffB
    }
}