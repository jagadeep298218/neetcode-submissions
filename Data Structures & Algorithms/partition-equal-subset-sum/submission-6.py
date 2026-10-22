class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = 0
        for i in range(len(nums)):
            total += nums[i]
        if total % 2 == 1:                  # odd total can't split into two equal halves
            return False
        target = total // 2
        memo = {}

        def dp(index, s):
            if s == target:                 # found a subset that makes half
                return True
            if s > target or index == len(nums):
                return False
            if (index, s) in memo:
                return memo[(index, s)]

            take = dp(index + 1, s + nums[index])    # use nums[index] (once -> index+1)
            skip = dp(index + 1, s)                  # don't use it
            memo[(index, s)] = take or skip
            return memo[(index, s)]

        return dp(0, 0)

