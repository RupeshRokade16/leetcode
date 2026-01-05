"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        """
        [5, 10], [15, 20], [0, 30], [0, 40] 

        Maybe I need to initialize a days list
        [[]] * len(intervals) (you actually do not need lists, instead just the lastEnding)

        Everytime there's a conflict you use the next day to check if that meeting can
        be accomodated on that day

        Alternate solution - Create a number line, initialized to 0
        Then go through the overlap, mark all numbers + 1 when encountered
        return the max number of such a list
        May not be ideal since the values go from 0 to 1,000,000


        """
        #sort by earliest finish
        intervals.sort(key = lambda x:x.start)

        days = [[] for i in range(len(intervals))]

        if not intervals: return 0
        print([(interval.start, interval.end) for interval in intervals])
        days[0].append(intervals[0].end)

        for interval in intervals[1:]:
            
            for j in range(len(days)):
                if days[j]:
                    if days[j][-1] <= interval.start:
                        days[j][-1] = interval.end
                        break
                else:
                    days[j].append(interval.end)
                    break
            

        maxDays = 0
        print(days)
        for i in range(len(days)):
            if days[i]:
                maxDays += 1

        return maxDays

        """
        Neetcode Solution: T:O(nlogn), S: O(n)

        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        res, count = 0, 0
        #count holds number of meetings going on at any given time

        s, e = 0, 0     #2 ptrs, for positions at start and end array respectively

        while s < len(intervals):   #s will reach end before e because start is before end time
            if start[s] < end[s]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1

            res = max(res, count)

        return res
        """
    

        """
        A great minHeap solution where you push lastEnding time to heap
        and you pop only when top of the minHeap can accomodate the current meeting
        The len of the minHeap gives the solution.

        T: O(nlogn), S:O(n)
        Time is n logn coz you might have to push n times to minHeap

        class Solution:
            def minMeetingRooms(self, intervals: List[Interval]) -> int:
                intervals.sort(key=lambda x: x.start)
                min_heap = []

                for interval in intervals:
                    if min_heap and min_heap[0] <= interval.start:
                        heapq.heappop(min_heap)
                    heapq.heappush(min_heap, interval.end)

                return len(min_heap)
        
        """
