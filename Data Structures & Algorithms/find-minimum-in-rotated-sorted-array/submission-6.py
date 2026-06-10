class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        if (nums[left] <= nums[right]):
            return nums[0]
        
        min = nums[right]
        
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < min:
                min = nums[mid]
                right = mid - 1
            else:
                left = mid + 1
        
        return min
        
        

        


