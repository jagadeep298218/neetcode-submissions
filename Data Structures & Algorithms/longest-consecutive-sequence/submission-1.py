class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) == 0:
            return 0
        longn = 1
        longest = 1

        for i in range(1, len(nums)):
            diff = nums[i] - nums[i - 1]
            if diff == 1:
                longn += 1
            elif diff == 0:
                continue
            else: 
                if longn > longest:
                    longest = longn
                longn = 1
        

        return max(longn, longest)