func countCharacters(words []string, chars string) int {

    charsMap := make(map[string]int)
    result := 0

    for i := 0; i < len(chars); i++ {
        charsMap[string(chars[i])]++
    }

    for j := 0; j < len(words); j++ {
        charsMapCopy := make(map[string]int)
        for k, v := range charsMap {
            charsMapCopy[k] = v
        }
        valid := true

        for k := 0; k < len(words[j]); k++ {
            _, exists := charsMapCopy[string(words[j][k])]
            if ((!exists) || (charsMapCopy[string(words[j][k])] - 1 < 0)) {
                valid = false
                break
            }
            charsMapCopy[string(words[j][k])]--
        }

        if valid {
            result += len(words[j])
        }
    }

    return result
}