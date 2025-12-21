class Solution {
    fun isPalindrome(x: Int): Boolean {
        if (x < 0) return false
        val strInt = x.toString()
        var l = 0;
        var r = strInt.length - 1
        while (l < r) {
            if (strInt[l] != strInt[r]) {
                return false
            }
            ++l
            --r
        }
        return true
    }
}