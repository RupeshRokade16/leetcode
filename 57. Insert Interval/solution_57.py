class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Overthought this solution a lot

        Just think 3 cases
        curr interval is purely to the right of the newInterval
        curr interval is purely to the left of the newInterval
        overlap
        """

        res = []
        newStart, newEnd = newInterval

        for i in range(len(intervals)):
            start, end = intervals[i]
            if newEnd < start:
                print("newEnd < start", newEnd, res)
                res.append(newInterval)
                return res + intervals[i:]
            elif newStart > end:
                res.append(intervals[i])
            else:
                #Overlap present
                newStart = min(newStart, start)
                newEnd = max(end, newEnd)
                newInterval = [newStart, newEnd]

        res.append([newStart, newEnd])
        return res
