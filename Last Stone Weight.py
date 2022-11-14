class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        # convert values to neg so minHeap is treated as maxHeap
        for stone in stones:
            maxHeap.append(-1 * stone)
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            stone1 = -1 * heapq.heappop(maxHeap)
            stone2 = -1 * heapq.heappop(maxHeap)
            #if x == y  both stones are destroyed so do nothing
            if stone1 != stone2:
                if stone1 > stone2:
                    newStone = stone1 - stone2
                    heapq.heappush(maxHeap, -1 * newStone)
                else:
                    newStone = stone2 - stone1
                    heapq.heappush(maxHeap, -1 * newStone)
        if maxHeap:
            output = -1 * heapq.heappop(maxHeap)
            return output
        else: # no stones left
            return 0
