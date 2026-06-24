class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        L = len(nums) 
        memo = {}
        res = []
        check = 0
        for i in nums:
            check += i
        if check%2 == 1:
            return False
        check /= 2

        
        def memoization(arr, s, level):
            if s == check:
                res.append(arr[:])
                return 
            if s > check or level == L:
                return 
            if (level, s) in memo:
                return memo[(level, s)]
            #skip i
            memo[level, s] = memoization(arr, s, level+1)
            
            #include i
            memo[level+1, s+nums[level]] = memoization(arr + nums[level:level+1], s+nums[level], level+1)
         

        memoization([], 0, 0)
        
        if len(res) > 0:
            return True
        else:
            return False
