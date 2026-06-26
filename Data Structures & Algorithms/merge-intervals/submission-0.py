class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:[x])
        res = []
        if not intervals:
            return []
        if len(intervals) == 1:
            return intervals
        for i in range(1,len(intervals)):
            if intervals[i-1][1] < intervals[i][0]:
                res.append(intervals[i-1])
            elif intervals[i-1][0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                intervals[i] = [min(intervals[i][0], intervals[i-1][0]), max(intervals[i][1], intervals[i-1][1])]
        res.append(intervals[i])
        return res