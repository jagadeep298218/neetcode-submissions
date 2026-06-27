class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        curr = res = nums[0]
        for i in nums[1:]:
            curr = max(i, curr+i)
            res = max(res, curr)

        return res