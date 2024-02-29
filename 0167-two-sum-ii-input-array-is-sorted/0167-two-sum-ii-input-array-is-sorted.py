class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        def binarySearch(l, r, tgt):
            mid = l + ((r-l)//2)
            while l < r:
                if numbers[mid] == tgt: return mid
                elif numbers[mid] > tgt: r = mid - 1
                else: l = mid + 1
                mid = l + ((r-l)//2)
            return mid if numbers[mid] == tgt else -1

        for idx, num in enumerate(numbers):
            tgt = target - num
            
            if tgt >= num:
                if idx == len(numbers) - 1:
                    continue
                res = binarySearch(idx + 1, len(numbers) -1, tgt)
                if res != -1:
                    return [idx+1, res+1]

            else:
                if idx == 0:
                    continue
                res = binarySearch(0, idx - 1, tgt)
                if res != -1:
                    return [idx+1, res+1]