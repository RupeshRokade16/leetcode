class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        2 tasks with same label, eg A, A -> then a gap of n 
        eg A, A, A, B, B, B -> 
            A -> B -> idle -> idle -> A -> B -> idle -> idle -> A ...

        Can build a frequency map, but how to use it efficiently?

        Most useful constraint -> n
        During n iterations, we can not repeat the same task
        So a window of n has to be unique

        What if I store freq and task name in a heap?
        During same values, it will choose and arbitrary value which wont be optimal

        Every value in heap can be benefit in knowing the iteration number say t
        Say from example 2, we choose A

        and add it back to the heap with t = t + n (it'll be a minheap)
        we increment t by 1
        then comes the second valid value, B -> add it back with t = t + n 

        So the question now is, how do we initialize these values?
        We choose each key from a freq map, add it to the minHeap and start processing
        We only add an element back to the minHeap if their count is nonZero

        The only problem now is, how to arrange the minHeap such that it will consume
        the most frequent element(s) first

        What I missed, suppose we have A repeating 4 times, B, C, D once and n = 1
        At such times, we need to make sure our most frequent element comes to the
        top of the heap (or priority queue)

        This means we make a queue + maxHeap to solve this
        maxHeap - built using count
        queue - built so that anytime a previously popped task becomes available, we add it back to maxHeap

        Tried using the heapq.heapify_max library additions but it isnt working
        for heapq.heappush_max

        """

        freqMap = defaultdict(int)

        for task in tasks:
            freqMap[task] += 1
        
        maxHeap = []

        for k, v in freqMap.items():
            maxHeap.append(-v)    #count

        heapq.heapify(maxHeap)
        queue = deque()     #contains a pair of cnt, new_valid_time

        t = 0
        while maxHeap or queue:
            t += 1

            if maxHeap:
                count = heapq.heappop(maxHeap) + 1  #logically -1
                if count:
                    queue.append([count, t + n]) #new time at which this task will be available 

            #Add back to the heap once the queue's task is available for the current time    
            if queue and queue[0][1] == t:
                cnt, time = queue.popleft()
                heapq.heappush(maxHeap, cnt)

            
        
        return t
