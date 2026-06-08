class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = nums[:]
        heapq.heapify(heap)

        for i in range(k):
            lowest = heapq.heappop(heap)
            j = nums.index(lowest)
            nums[j] = lowest*multiplier
            heapq.heappush(heap, nums[j])
        
        return nums