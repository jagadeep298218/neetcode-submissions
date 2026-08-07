class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}

        for num in nums:
            hash[num] = hash.get(num, 0) + 1
        
        heap = []

        for num, count in hash.items():
            heapq.heappush(heap, [count, num])
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for i, j in heap:
            res.append(j)
        return res