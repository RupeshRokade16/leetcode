class KthLargest:
    """
    kth largest - maxHeap will get you largest not the kth largest
                - minHeap will hold n larger elements from an array. if you keep the
                  length of minHeap == k by popping n-k times, then it will hold top k elements, 
                  so minHeap[0] i.e the top of the heap will always show the kth largest element
                  which is actually the smallest element in the k sized heap 
    """

    def __init__(self, k: int, nums: List[int]):
        self.k, self.minHeap = k, nums
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        #This if block is just an optimization, where we can skip adding an small values
        if len(self.minHeap) == self.k and val < self.minHeap[0]:
            return self.minHeap[0]
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        return self.minHeap[0]
