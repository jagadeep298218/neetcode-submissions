"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        count, m = 0, 0
        while start and end:
            if start[0] < end[0]:
                count += 1
                start.pop(0)
            else:
                count -= 1
                end.pop(0)
            m = max(count, m)
        return m
