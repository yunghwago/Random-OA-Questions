class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #prim's algorithm solution
        #1. calculate all distances to all unvisited nodes from a starting point
        #2. store those distances in a heap, then pop the min
        #3. add the point we were just at to a visited set, then repeat until all nodes are connected
        #4. we should finish when we have n-1 edges
        
        #create blank adjacency list because we weren't given it
        n = len(points)
        adj = {i:[] for i in range(n) } #i : [cost to travel to node, destination node]
        
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1,n):
                x2, y2 = points[j]
                #calculate manhattan distance
                distance = abs(x1-x2) + abs(y1-y2)
                adj[i].append([distance, j])
                adj[j].append([distance, i])
        #at this point adj should look like this:
        #0: distances to all points, 1: distances to all points... etc.
        
        #actual prim's algorithm part
        result = 0
        visit = set()
        minHeap = [[0,0]] #[cost to travel to node, destination node]
        while len(visit) < n:
            #remove the smallest distance amongst the distances of a point
            cost, i = heapq.heappop(minHeap)
            if i in visit:
                continue
            result += cost
            visit.add(i)
            for neighborCost, neighbor in adj[i]:
                if neighbor not in visit:
                    #push distance of every point from single point
                    heapq.heappush(minHeap, [neighborCost, neighbor])
                    
        return result
