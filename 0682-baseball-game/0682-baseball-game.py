class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        sum = 0
        for i in range(0, len(operations)):
            if operations[i] == '+':
                val = stack[len(stack) - 2] + stack[len(stack) - 1]
                sum += val
                stack.append(val)
            elif operations[i] == 'D':
                val = stack[len(stack) - 1] * 2
                sum += val
                stack.append(val)
            elif operations[i] == 'C':
                sum -= stack[len(stack) - 1]
                stack.pop()
            else:
                sum += int(operations[i])
                stack.append(int(operations[i]))

        return sum