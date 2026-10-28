class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        count = 0
        max_count = 0
        k_count = 0
        while right < len(nums):
            if nums[right] == 1:
                count += 1
            else:
                k_count += 1
                count += 1
            while k_count > k:
                if nums[left] == 0:
                    k_count -= 1
                count -= 1
                left += 1
            max_count = max(count, max_count)
            right += 1

        return max_count