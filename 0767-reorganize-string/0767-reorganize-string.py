class Solution:
    def reorganizeString(self, s: str) -> str:
        maxHeap = []
        occurences = {}

        for char in s:
            if char in occurences:
                occurences[char] += 1
            else:
                occurences[char] = 1

        for char, occ in occurences.items():
            heapq.heappush(maxHeap, (-occ, char))

        res = ""

        while maxHeap:
            
            if len(maxHeap) == 1:
                last = heapq.heappop(maxHeap)
                if last[0] < -1: return ""
                else: return res + last[1]

            else:
                curr1 = list(heapq.heappop(maxHeap))
                curr2 = list(heapq.heappop(maxHeap))

                res += curr1[1]
                curr1[0] += 1
                res += curr2[1]
                curr2[0] += 1
                if curr1[0] <= -1:
                    heapq.heappush(maxHeap, tuple(curr1))
                if curr2[0] <= -1:
                    heapq.heappush(maxHeap, tuple(curr2))

        return res