func maxScore(s string) int {
    right := 0
    maxScore := 0

    for i := 1; i < len(s); i++ {
        if string(s[i]) == "1" {
            right++
        }
    }

    maxScore = right
    left := 0

    for i := 0; i < len(s) - 1; i++ {
        if string(s[i]) == "0" {
            left++
        } else if string(s[i]) == "1" {
            if i == 0 {
                continue
            }
            right--
        }
        if left + right > maxScore {
            maxScore = left + right
        }
    }
    return maxScore
}