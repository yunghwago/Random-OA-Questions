class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []
        for number in nums:
            maxHeap.append(-number)
        heapq.heapify(maxHeap)
        while k > 0:
            output = heapq.heappop(maxHeap)
            k -= 1
        return output * -1
