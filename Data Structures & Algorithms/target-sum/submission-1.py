class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        L = len(nums)

        def memoization(level, val):
            if level == L:
                if val == target: return 1
                return 0

            
            if (level, val) in memo:
                return memo[(level, val)]
            
            # exclude i
            memo[(level, val)] = memoization(level+1, val-nums[level]) + memoization(level+1, val+nums[level])
            return memo[(level, val)]
        return memoization(0, 0)
