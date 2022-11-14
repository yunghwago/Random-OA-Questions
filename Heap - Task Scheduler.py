class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #note we
        maxHeap = [] #holds all of the remaining characters that exist
        #does not need to be a tuple because we don't need to return
        #the sequence of characters themselves
        
        queue = deque() #holds characters that need to wait until they
        #can be executed again
        #tuple = (count of character, timestamp indicating when it can
        #go back into maxHeap)
        
        time = 0
        
        temp = Counter(tasks) #get count of every letter
        for task in temp:
            maxHeap.append(-1* temp[task])
        
        heapq.heapify(maxHeap)
        while maxHeap or queue:
            if maxHeap:
                currentTask = heapq.heappop(maxHeap)
                if currentTask + 1 < 0: #not the last letter
                    queue.append((currentTask + 1, time + n))
            if queue:
                if time == queue[0][1]: #time == queue's front item timestamp
                    task, tTime = queue.popleft()
                    if task != 0:
                        heapq.heappush(maxHeap, task)
            time += 1
        return time
Console
