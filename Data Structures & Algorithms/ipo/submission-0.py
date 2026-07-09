class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        minheap, maxheap = [], []
        # (capital, profit)

        for i in range(len(capital)):
            heapq.heappush(minheap, [capital[i], profits[i]])
        
        while k > 0:
            while minheap and minheap[0][0] <= w:
                val= heapq.heappop(minheap)
                heapq.heappush(maxheap, [-val[1], val[0]])
            if maxheap:
                val = heapq.heappop(maxheap)
            else:
                return w
            w += (-val[0])
            k -= 1
        return w
