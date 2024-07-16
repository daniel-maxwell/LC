func makeGood(s string) string {
    
    strSlice := []string{}

    for i := 0; i < len(s); i++ {
        strSlice = append(strSlice, string(s[i]))
    }
    
    for true {
        deletions := 0

        l := len(strSlice) - 2

        for l >= 0 {
            r := l + 1

            if (strSlice[l] != strSlice[r] && 
                strings.ToLower(strSlice[l]) == strings.ToLower(strSlice[r])) {
                    strSlice[l] = " "
                    strSlice[r] = " "
            }
            l--
            if l == -1 || r == -1{
                break
            }
        }

        tempSlice := []string{}

        for i := 0; i < len(strSlice); i++ {
            if string(strSlice[i]) != " " {
                tempSlice = append(tempSlice, string(strSlice[i]))
            } else {
                deletions++
            }
        }
        strSlice = tempSlice
        if deletions == 0 {
            break
        }
    }

    return strings.Join(strSlice, "")
}