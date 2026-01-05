class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        How to differentiate and remove intervals?

        For eg, intervals = [[1, 2], [1, 3], [2, 3], [3, 4]]
        lastEnding = 2
        
        [1, 11], [1, 100], [2, 12], [11, 22]

        Try to remove the one that doesnt end early
        
        """
        intervals.sort(key= lambda x:(x[0], x[1]))
        res = 0
        lastEnding = intervals[0][1]

        for start, end in intervals[1:]:
            #non overlap
            if start >= lastEnding:
                lastEnding = end
            else:
                #Remove overlap
                res += 1
                lastEnding = min(end, lastEnding) #we keep earliest ending

        return res
