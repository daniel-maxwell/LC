class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tempStack = [(temperatures[0], 0)]
        output = [0] * len(temperatures)

        for i in range(1, len(temperatures)):
            while len(tempStack) > 0 and temperatures[i] > tempStack[-1][0]:
                output[tempStack[-1][1]] = (i - tempStack[-1][1])
                tempStack.pop()
            tempStack.append((temperatures[i], i))

        return output