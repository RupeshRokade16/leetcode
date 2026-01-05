"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals.sort(key = lambda x: x.start)
        if not intervals: return True

        lastEnding = intervals[0].end

        for interval in intervals[1:]:
            
            if lastEnding > interval.start:
                return False
            else:
                lastEnding = interval.end

        return True
    