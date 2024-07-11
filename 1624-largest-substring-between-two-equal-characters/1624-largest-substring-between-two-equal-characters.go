func maxLengthBetweenEqualCharacters(s string) int {
    charMap := make(map[rune][]int)

    for i, char := range s {
        if _, isPresent := charMap[char]; isPresent {
            charMap[char][1] = i
        } else {
            charMap[char] = []int{i, -1}
        }
    }

    result := -1

    for _, v := range(charMap) {
        if v[1] == -1 {
            continue
        } else {
            dist := v[1] - v[0] - 1
            if dist > result {
                result = dist
            }
        }
    }

    return result
}