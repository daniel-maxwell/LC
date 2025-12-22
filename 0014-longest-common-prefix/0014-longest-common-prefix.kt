class Solution {
    fun longestCommonPrefix(strs: Array<String>): String {
        if (strs.size == 0) return ""
        val prefixBuilder = StringBuilder()
        var i = 0;
        while (i < strs[0].length) {
            val c = strs[0][i];
            for (s in strs) {
                if (i >= s.length || s[i] != c) {
                    return prefixBuilder.toString()
                }
            }
            prefixBuilder.append(c)
            ++i
        }
        return prefixBuilder.toString()
    }
}