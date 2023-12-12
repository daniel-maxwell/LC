class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        mainHeap, bufferHeap, res,  time = [], [], [], float('inf')

        # Add idx of each task and populate Main Heap with each task
        # Each task has the format [enqueueTime, processingTime, index]
        for i in range(0, len(tasks)):
            if tasks[i][0] < time: time = tasks[i][0]
            tasks[i].append(i)
            mainHeap.append(tasks[i])
        heapq.heapify(mainHeap)

        # Process tasks based on which tasks are <= current time, and update current time
        # With either the amount of time it took to process the current task
        # or the time the next task can be processed
        while mainHeap:
            while mainHeap and mainHeap[0][0] <= time:
                heapq.heappush(bufferHeap, heapq.heappop(mainHeap)[1:])
            
            if bufferHeap:
                currTask = heapq.heappop(bufferHeap)
                time += currTask[0]
                res.append(currTask[1])
            else:
                time = mainHeap[0][0]
        
        while bufferHeap:
            res.append(heapq.heappop(bufferHeap)[1])

        return res