func getRow(rowIndex int) []int {
    var s = make([]int, 1)
    s[0] = 1

    for i := 0; i < rowIndex; i++ {
        newS := make([]int, len(s) + 1)
        for j := 0; j < len(newS); j++ {
            a, b := 0, 0
            if j - 1 >= 0 {
                a = s[j-1]
            }
            if j < len(s) {
                b = s[j]
            }
            newS[j] = a + b
        }
        s = newS
    }
    return s
}