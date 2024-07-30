func findAnagrams(s string, p string) []int {
    pMap := make(map[string]int)
    sMap := map[string]int{ string(s[0]): 1 }
    for i := 0; i < len(p); i++ {
        pMap[string(p[i])]++
    }
    result := []int{}
    l, r := 0, 1

    for r < len(s) {
        if r - l == len(p) {
            if reflect.DeepEqual(sMap, pMap) {
                result = append(result, l)
            }
            sMap[string(s[l])]--
            if sMap[string(s[l])] == 0 {
                delete(sMap, string(s[l]))
            }
            l++
        } else {
            sMap[string(s[r])]++
            r++
        }
    }
    
    if reflect.DeepEqual(sMap, pMap) {
                result = append(result, l)
    }
    return result
}