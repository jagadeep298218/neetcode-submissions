class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        create_set = set()
        for i in nums:
            if (i in create_set):
                return True
            else: create_set.add(i)
        
        return False