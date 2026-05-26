class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        geek = set()
        for num in nums:
            if num in geek:
                return True
            geek.add(num)

        return False