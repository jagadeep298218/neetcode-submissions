class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals += [newInterval]

        intervals.sort()
        res = []
        for begin, end in intervals:
            if not res:
                res.append([begin, end])
            if res[-1][1] >= begin:
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append([begin, end])
        return res