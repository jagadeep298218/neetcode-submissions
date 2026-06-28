class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump = float("-inf")
        for i in range(len(nums)):
            if i == len(nums)-1:
                return True
            if nums[i] > jump:
                jump = nums[i]
            if jump == 0:
                return False 
            jump -= 1       
        return True
        
