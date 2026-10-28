class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        res = []
        maxheap = []

        for right in range(len(nums)):
            heapq.heappush(maxheap, (-nums[right], right))

            if (right-left+1) == k:
                res.append(-maxheap[0][0])
                if left == maxheap[0][1]:
                    heapq.heappop(maxheap)
                left += 1
            while maxheap and maxheap[0][1] < left:
                heapq.heappop(maxheap)
        return res