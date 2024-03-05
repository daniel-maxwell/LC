class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack, i = [], 0

        while i < len(asteroids):
            asteroid = asteroids[i]

            if not stack:
                stack.append(asteroid)

            elif stack[-1] >= 0 and asteroid < 0:
                while stack:
                    if stack[-1] < 0 and asteroid < 0:
                        stack.append(asteroid)
                        break
                    elif stack[-1] > abs(asteroid):
                        break
                    elif stack[-1] == abs(asteroid):
                        stack.pop()
                        break
                    else:
                        stack.pop()
                        if not stack:
                            stack.append(asteroid)
                            break
                
            else:
                stack.append(asteroid)

            i += 1

        return stack