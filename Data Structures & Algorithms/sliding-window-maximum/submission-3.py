class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        res = []
        queue = deque()

        for right in range(len(nums)):
            while queue and nums[queue[-1]] < nums[right]:
                queue.pop()
            queue.append(right)
            while queue[0] < left:
                queue.popleft()
            
            if right-left + 1 == k:
                res.append(nums[queue[0]])
                left += 1
            
        
        return res
            
            