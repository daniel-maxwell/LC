class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        def insertMaxHeap(self, heap, val):
            pos = len(heap)
            heap.append(val)
            parentIdx = floor((pos-1) / 2)

            while pos > 0 and heap[parentIdx] < heap[pos]: 
                heap[parentIdx], heap[pos] = heap[pos], heap[parentIdx]
                pos = parentIdx
                parentIdx = floor((pos-1) / 2)

        for num in nums:
            insertMaxHeap(self, heap, num)

        def extractMax(heap):
            MAX, heap[0] = heap[0], heap[-1]
            heap.pop()
            maxHeapify(heap, 0)
            return MAX

        def maxHeapify(heap, root):
            largest = index_largest_node(root)
            if largest != root:
                heap[largest], heap[root] = heap[root], heap[largest]
                maxHeapify(heap, largest)

        def index_largest_node(rootIndex):
            left_child = heap[(2 * rootIndex) + 1] if len(heap) > (2 * rootIndex) + 1 else float('-inf')
            right_child = heap[(2 * rootIndex) + 2] if len(heap) > (2 * rootIndex) + 2 else float('-inf')

            if (heap[rootIndex] >= left_child and heap[rootIndex] >= right_child):
                return rootIndex
            elif (left_child >= heap[rootIndex] and left_child >= right_child):
                return (2 * rootIndex) + 1
            else:
                return (2 * rootIndex) + 2

        while k > 1:
            extractMax(heap)
            k -= 1

        return heap[0]