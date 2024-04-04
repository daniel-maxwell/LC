class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:

        def processTasks(t):
    
            while busyServerHeap and t >= busyServerHeap[0][0]: # remove all free servers from busy server heap
                freeServer = heapq.heappop(busyServerHeap)
                heapq.heappush(serverHeap, (freeServer[1], freeServer[2]))

            while serverHeap and taskQueue: # while we have free servers and tasks to complete...
                server = heapq.heappop(serverHeap)
                task = taskQueue.popleft()
                serverInUse = (t + task, server[0], server[1])
                heapq.heappush(busyServerHeap, serverInUse)
                result.append(server[1])

            if busyServerHeap:
                return busyServerHeap[0][0]
            else:
                return t + 1
        
        serverHeap = [(weight, idx) for idx, weight in enumerate(servers)]
        busyServerHeap = []
        heapq.heapify(serverHeap)
        heapq.heapify(busyServerHeap)
        taskQueue = deque([])
        result = []

        for t in range(len(tasks)):
            taskQueue.append(tasks[t])
            processTasks(t)

        nextAvailableTime = len(tasks)

        while taskQueue:
            nextAvailableTime = processTasks(nextAvailableTime)
            
        return result