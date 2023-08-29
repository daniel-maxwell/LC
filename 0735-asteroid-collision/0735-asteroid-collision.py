class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack, output = [], []

        for i in range(0, len(asteroids)):
            
            if asteroids[i] < 0:
                if not stack:
                    output.append(asteroids[i])
                else:
                    while stack:
                        if stack[-1] < abs(asteroids[i]):
                            stack.pop()

                        elif stack[-1] == abs(asteroids[i]):
                            stack.pop()
                            break

                        else:
                            break
                    else:
                        if not stack:
                            output.append(asteroids[i])
            else:
                stack.append(asteroids[i])

        return output + stack