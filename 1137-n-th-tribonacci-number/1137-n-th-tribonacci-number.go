func tribonacci(n int) int {
    trib := [3]int{0, 1, 1}
    if n < len(trib) {
        return trib[n]  
    }

    i := 2
    for i < n {
        temp := trib[0] + trib[1] + trib[2]
        trib[0] = trib[1]
        trib[1] = trib[2]
        trib[2] = temp
        i++
    }

    return trib[2]
}