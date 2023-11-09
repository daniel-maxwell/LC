class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = set(['+', '-', '*', '/'])
        def evaluate(a, b, operator):
            if operator == '+':
                return a + b
            if operator == '-':
                return a - b
            if operator == '*':
                return a * b
            if operator == '/':
                return math.trunc(a / b)

        stack = []
        for token in tokens:
 
            if token not in operators:
                stack.append(token)

            else:
                valB = int(stack.pop())
                valA = int(stack.pop())
                stack.append(str(evaluate(valA, valB, token)))
            
        return int(stack.pop())