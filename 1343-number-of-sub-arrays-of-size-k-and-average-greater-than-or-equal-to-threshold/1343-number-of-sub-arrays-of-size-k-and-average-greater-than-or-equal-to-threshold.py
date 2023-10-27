class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        threshold = threshold * k
        l, r, sum = 0, 0, 0

        for r in range(0, k):
            sum += arr[r]

        res = 1 if sum >= threshold else 0
        
        while r + 1 < len(arr):
            sum -= arr[l]
            l += 1
            r += 1
            sum += arr[r]

            if sum >= threshold:
                res += 1

        return res