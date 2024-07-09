func isPalindrome(s string) bool {
    l, r := 0, len(s) - 1

    for l <= r {

        if !regexp.MustCompile(`^[a-zA-Z0-9]*$`).MatchString(string(s[l])) {
            l++
            continue
        } else if !regexp.MustCompile(`^[a-zA-Z0-9]*$`).MatchString(string(s[r])) {
            r--
            continue
        }
        if strings.ToLower(string(s[l])) != strings.ToLower(string(s[r])) {
            return false
        }
        l++
        r--
    }
    return true
}