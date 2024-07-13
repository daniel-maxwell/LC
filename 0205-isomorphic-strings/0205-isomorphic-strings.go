func isIsomorphic(s string, t string) bool {
    if len(s) != len(t) {
        return false
    }

    sToT := make(map[byte]byte)
    tToS := make(map[byte]byte)

    for i := 0; i < len(s); i++ {
        val, present := sToT[s[i]]
        if present && val != t[i] {
            return false
        }
        sToT[s[i]] = t[i]

        val, present = tToS[t[i]]
        if present && val != s[i] {
            return false
        }
        tToS[t[i]] = s[i]
    }
    return true
}