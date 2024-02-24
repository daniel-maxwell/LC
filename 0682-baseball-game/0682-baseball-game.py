class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []

        for i in range(len(operations)):

            if operations[i] == '+':
                scores.append(scores[-1] + scores[-2])

            elif operations[i] == 'D':
                scores.append(scores[-1] * 2)

            elif operations[i] == 'C':
                scores.pop()

            else:
                scores.append(int(operations[i]))

        return sum(scores)