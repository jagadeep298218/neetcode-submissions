class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''
        either choose a number or skip and store sum?
        '''
        
        def dp(sum1, sum2, index):
            if sum1 == sum2 and index == len(nums):
                return True
            if index >= len(nums):
                return False
            if (sum1, sum2, index) in memo:
                return memo[(sum1, sum2, index)]
            memo[(sum1, sum2, index)] =  dp(nums[index] + sum1, sum2, index+1) or dp(sum1, nums[index] + sum2, index+1)
            return memo[(sum1, sum2, index)]

        memo = {}
        return dp(0, 0, 0)

        