class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tempQueue = [(temperatures[0], 0)]
        output = [0] * len(temperatures)

        for i in range(1, len(temperatures)):
            while len(tempQueue) > 0 and temperatures[i] > tempQueue[-1][0]:
                output[tempQueue[-1][1]] = (i - tempQueue[-1][1])
                tempQueue.pop()
            tempQueue.append((temperatures[i], i))

        return output