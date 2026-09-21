"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

record all end times of diff rooms
check w lowest end time if needed to add another room
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x.start)
        min_heap = []
        heapq.heappush(min_heap, intervals[0].end)
        rooms = 1
        for x in intervals[1:]:
            if x.start < min_heap[0]:
                heapq.heappush(min_heap, x.end)
                rooms += 1
            else:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, x.end)
        return rooms



        