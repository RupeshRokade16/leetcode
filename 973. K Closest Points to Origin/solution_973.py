class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x1,y1 in points:
            dist = sqrt(x1*x1 + y1*y1)
            minHeap.append((dist, x1, y1))

        heapq.heapify(minHeap)
        res = []

        while minHeap and k:
            dist, x, y = heapq.heappop(minHeap)

            k -= 1

            res.append((x,y))

        return res
