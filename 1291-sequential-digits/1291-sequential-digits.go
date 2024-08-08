func sequentialDigits(low int, high int) []int {

    splitToDigits := func(num int) []int {
        var digits []int
        numStr := strconv.Itoa(num)
        for _, char := range numStr {
            digit, _ := strconv.Atoi(string(char))
            digits = append(digits, digit)
        }
        return digits
    }

    combineDigits := func(digits []int) int {
	    var strDigits []string
        for _, digit := range digits {
            strDigits = append(strDigits, strconv.Itoa(digit))
        }
        numStr := strings.Join(strDigits, "")
        num, _ := strconv.Atoi(numStr)
	    return num
    }

    isSequential := func(digits []int) bool {
        for i := 1; i < len(digits); i++ {
            if digits[i] != digits[i-1] + 1 {
                return false
            }
        }
        return true
    }

    getNextSeqNum := func(num int) int {
        splitNum := splitToDigits(num)
        if isSequential(splitNum) {
            return num
        } else {
            for {
                for i := 1; i < len(splitNum); i++ {
                    splitNum[i] = splitNum[i-1] + 1
                    if splitNum[i] == 10 {
                        return -1
                    }
                }
                res := combineDigits(splitNum)
                if res > num {
                    return res
                } else {
                    splitNum[0]++
                }
            }
        }
        return 0
    }

    roundToNextPwr10 := func(n int) int {
        numDigits := int(math.Log10(float64(n))) + 1
        return int(math.Pow(10, float64(numDigits)))
    }

    result := []int{}

    for {
        if (int(math.Log10(float64(low))) + 1) > 9 {
            return result
        }
        num := getNextSeqNum(low)
        if num == -1 {
            low = roundToNextPwr10(low)
            continue
        }
        if num > high {
            return result
        } else {
            result = append(result, num)
            if (num + 1) % 10 == 0 {
                low = roundToNextPwr10(num)
            } else {
                low = num + 1
            }
        }
    }
    return result
}