class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashim = set()

        for num in nums:
            hashim.add(num)
        return len(hashim) < len(nums)