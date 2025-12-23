class Solution {
    fun isValid(s: String): Boolean {
        val stack = ArrayDeque<Char>()
        val parenthesisMap = mapOf<Char, Char> (
            ')' to '(',
            ']' to '[',
            '}' to '{'
        )
        for (c in s) {
            if (c in parenthesisMap) {
                val poppedValue = stack.removeLastOrNull()
                if (poppedValue != parenthesisMap.getValue(c)) {
                    println(poppedValue)
                    return false
                }
                continue
            }
            stack.addLast(c)
        }
        return stack.isEmpty()
    }
}