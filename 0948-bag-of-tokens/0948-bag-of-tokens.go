func bagOfTokensScore(tokens []int, power int) int {
    slices.Sort(tokens)
    l, r := 0, len(tokens) - 1
    score, maxScore := 0, 0

    for l <= r {
        if score == 0 && power < tokens[l] {
            break
        } else if power >= tokens[l] {
            power -= tokens[l]
            l++
            score++
            if score > maxScore { maxScore = score }
        } else {
            power += tokens[r]
            r--
            score--
        }
    }
    return maxScore
}