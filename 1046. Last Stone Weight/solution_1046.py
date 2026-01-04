class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        if not stones: return 0
        if len(stones) == 1: return stones[0]

        minHeap = [-1*x for x in stones]
        heapq.heapify(minHeap)


        while len(minHeap) >= 2:

            first, second = heapq.heappop(minHeap), heapq.heappop(minHeap)
            first *= -1
            second *= -1

            if first != second:
                heapq.heappush(minHeap, second - first)

        return -1 * minHeap[0] if minHeap else 0
