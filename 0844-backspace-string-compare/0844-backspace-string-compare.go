func backspaceCompare(s string, t string) bool {
    var hash byte = 35
    sStack, tStack := []byte{}, []byte{}

    for i := 0; i < len(s); i++ {
        if s[i] == hash {
            if len(sStack) > 0 {
                sStack = sStack[:len(sStack) - 1]
            }
        } else {
            sStack = append(sStack, s[i])
        }
    }

    for i := 0; i < len(t); i++ {
        if t[i] == hash {
            if len(tStack) > 0 {
                tStack = tStack[:len(tStack) - 1]
            }
        } else {
            tStack = append(tStack, t[i])
        }
    }
    
    return string(sStack) == string(tStack)
}