class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        remaining, substrCounts, i, j = {}, {}, 0, len(s1)

        for char in s1:
            if char not in remaining: remaining[char] = 1
            else: remaining[char] += 1

        totalRequired = remaining.copy()

        for char in s2[i:j]:
            if char in substrCounts: substrCounts[char] += 1
            else: substrCounts[char] = 1

            if char in remaining:
                remaining[char] -= 1
                if remaining[char] == 0: remaining.pop(char)

        if len(remaining) == 0: return True

        while j < len(s2):
            left, right = s2[i], s2[j]

            substrCounts[left] -= 1
            if substrCounts[left] == 0: substrCounts.pop(left)

            if right in substrCounts:
                substrCounts[right] += 1
            else: substrCounts[right] = 1

            if left in totalRequired:
                if left in remaining:
                    remaining[left] += 1
                else:
                    if totalRequired[left] - substrCounts.get(left, 0) == 1:
                        remaining[left] = 1

            if right in remaining:
                remaining[right] -= 1
                if remaining[right] == 0: remaining.pop(right)

            if len(remaining) == 0:
                return True
            i += 1
            j += 1

        return False