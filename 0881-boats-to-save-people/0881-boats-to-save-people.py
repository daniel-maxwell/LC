class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        right = len(people) - 1
        left = res = 0
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            res += 1
        return res