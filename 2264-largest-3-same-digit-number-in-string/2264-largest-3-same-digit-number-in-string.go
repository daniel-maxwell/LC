func largestGoodInteger(num string) string {
    largest := -1
    occ := 1

    currNum, err := strconv.Atoi(string(num[0]))
    if err != nil {
        return ""
    }

    for i := 1; i < len(num); i++ {
        if s, err := strconv.Atoi(string(num[i])); s == currNum {
            if err != nil {
                return ""
            }
            occ++
        } else {
            occ = 1
            currNum, err = strconv.Atoi(string(num[i]))
            if err != nil {
                return ""
            }
        }
        if occ == 3 {
            currNumStr := strconv.Itoa(currNum)
            fullNum, err := strconv.Atoi(strings.Repeat(currNumStr, 3))
            if err != nil {
                return ""
            }
            if fullNum > largest {
                largest = fullNum
            }
        }
    }

    if largest == -1 {
        return ""
    } else if largest == 0 {
        return strings.Repeat("0", 3)
    } else {
        return strconv.Itoa(largest)
    }
}