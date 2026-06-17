from decimal import Decimal
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        dist = {}
        val = []
        for x, y in points:
            d = math.sqrt((x - 0)**2 + (y - 0)**2)
            dist.setdefault(d, []).append([x, y])
            val.append([d, x, y]) 
        
        heapq.heapify(val)

        while k > 0:
            x = heapq.heappop(val)
            res.append(x[1:3])
            k-=1
        return res