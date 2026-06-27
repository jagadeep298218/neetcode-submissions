"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x:x.start)
        res = [intervals[0].end]
        for interval in intervals[1:]:
            add = True
            start, end = interval.start, interval.end
            for endTime in range(len(res)):
                if start >= res[endTime]:
                    res[endTime] = max(end, res[endTime])
                    add = False
                    break
            if add:
                res.append(end)
        
        return len(res)
                
