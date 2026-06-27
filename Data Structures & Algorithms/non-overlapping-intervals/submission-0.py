class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x:x[1])
        if not intervals:
            return 0
        res = []
        count = 0
        res.append(intervals[0])
        for start, end in intervals[1:]:
            if start < res[-1][1]:
                count+=1 
            else:
                res.append([start,end])
        return count