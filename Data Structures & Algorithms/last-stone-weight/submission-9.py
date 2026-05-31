class Solution:
    import heapq

    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 0:
            return 0
            
        for i in range(len(stones)):
            stones[i] = -stones[i]

        heapq.heapify(stones)

        while len(stones) > 1:
            heapq.heappush(stones, heapq.heappop(stones) - (heapq.heappop(stones)))
        
        return -stones[0]
            
        
        



        
            
        
        