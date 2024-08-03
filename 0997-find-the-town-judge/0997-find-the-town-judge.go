func findJudge(n int, trust [][]int) int {
    if len(trust) == 0 {
        if n == 1 {
            return 1
        } else {
            return -1
        }
    }
    trustedPeople := map[int][]int{}
    trustingPeople := map[int][]int{}

    for _, rel := range trust {
        trustedPeople[rel[1]] = append(trustedPeople[rel[1]], rel[0])
        trustingPeople[rel[0]] = append(trustedPeople[rel[0]], rel[1])
    }

    for k, v := range trustedPeople {
        if len(v) == n - 1 {
            if _, exists := trustingPeople[k]; !exists {
                return k
            }
        }
    }
    return -1
}