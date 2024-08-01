func evalRPN(tokens []string) int {

    operators := map[string]bool{
        "+": true,
        "-": true,
        "*": true,
        "/": true,
    }

    var eval = func(a int, b int, operator string) int {
        switch {
            case operator == "+":
                return a + b
            case operator == "-":
                return a - b
            case operator == "*":
                return a * b
            case operator == "/":
                return a / b
            default:
                return a + b
        }
    }

    stack := []int{}

    for _, byteToken := range tokens {
        token := string(byteToken)
        if _, exists := operators[token]; exists {
            a, b := stack[len(stack) - 2], stack[len(stack) - 1]
            stack = stack[:len(stack) - 2]
            stack = append(stack, eval(a, b, token))
        } else {
            val, err := strconv.Atoi(token)
            if err != nil { 
                fmt.Println("Atoi Conversion error")
                return 0
            }
            stack = append(stack, val)
        }
    }
    return stack[0]
}