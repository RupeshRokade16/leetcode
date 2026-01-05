class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ascending = sorted(intervals, key = lambda x:x[0])
        res = []

        
        i = 0
        first = ascending[0]
        second = 0
        while i + 1< len(ascending):
            second = ascending[i + 1]
            print(first, second)
            #No overlap, append old
            if first[1] < second[0]:
                res.append(first)
                first = second

            #if overlap, compute merged interval, store in first, second will now be interval[i]
            if first[1] >= second[0]:
                first[0] = min(first[0], second[0])
                first[1] = max(first[1], second[1])
            
            i += 1
        res.append(first)
        return res
                
        """Cleaner Code
        
        intervals.sort(key = lambda x:x[0])
        res = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnding = res[-1][1]

            if lastEnding >= start:
                res[-1][1] = max(lastEnding, end)
            else:
                res.append([start, end])

        return res
        """
