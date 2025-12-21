class Solution {
    fun romanToInt(s: String): Int {
        val numeralMap = mapOf(
            'I' to 1,
            'V' to 5,
            'X' to 10,
            'L' to 50,
            'C' to 100,
            'D' to 500,
            'M' to 1000,
        )
        val subtractMap: Map<Char, Set<Char>> = mapOf(
            'I' to setOf('V', 'X'),
            'X' to setOf('L', 'C'),
            'C' to setOf('D', 'M')
        )

        var result = 0
        var idx = s.length - 1

        while (idx >= 0) {
            result += numeralMap.getValue(s[idx])
            if (idx - 1 >= 0 && s[idx] in subtractMap[s[idx - 1]].orEmpty()) {
                result -= numeralMap.getValue(s[idx - 1])
                idx -= 2
            } else {
                idx -= 1
            }
        } 

        return result
    }
}