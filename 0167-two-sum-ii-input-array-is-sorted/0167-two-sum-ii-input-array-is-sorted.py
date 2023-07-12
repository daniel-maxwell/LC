class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)

        for i in range(0, length):
            low = i+1
            high = length-1
            mid = math.floor((high + low) / 2)

            while high - low > 1:

                if numbers[i] + numbers[mid] > target:
                    high = mid
                    mid = mid - max(1, math.floor((high - low) / 2))
                
                elif numbers[i] + numbers[mid] < target:
                    low = mid
                    mid = mid + max(1, math.floor((high - low) / 2))
                
                else: return [i+1, mid+1]
                
            else:
                if numbers[i] + numbers[mid] == target:
                    return [i+1, mid+1]
                elif numbers[i] + numbers[high] == target:
                    return [i+1, high+1]
