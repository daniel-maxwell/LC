func findContentChildren(g []int, s []int) int {

    slices.Sort(g)
    slices.Sort(s)
    result := 0 

    i := len(s) - 1

    for i >= 0 {
        if s[i] >= g[len(g) - 1] {
            result++
            i--
        }
        g = g[:len(g) - 1]
        if len(g) == 0 {
            break
        }
    }

    return result
}