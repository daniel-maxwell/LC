class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        numBoats, rescued = 0, 0
        numToRescue = len(people)

        while rescued < numToRescue:
            heaviest = people.pop()
            rescued += 1
            peopleToCheck = len(people)

            # Select heaviest person under weight limit (if any)
            # Binary search

            l, r = 0, len(people) - 1
            mid = l + (r - l)//2

            while peopleToCheck >= 1 and mid >= 0:
                
                combinedWeight = people[mid] + heaviest

                if combinedWeight <= limit:
                    if mid+1 >= len(people):
                        break
                    elif people[mid+1] + heaviest > limit:
                        break
                    else:
                        l = mid + 1
                else:
                    r = mid - 1
                    
                mid = l + (r - l)//2               
                peopleToCheck -= 1
            
            if peopleToCheck > 0 and mid >= 0: # We found a second person
                people.pop(mid)
                rescued += 1
            
            numBoats += 1

        return numBoats