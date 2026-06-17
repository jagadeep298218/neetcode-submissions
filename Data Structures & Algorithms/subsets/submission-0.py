class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def parse(val, level):
            if level == len(nums):
                res.append(val[:])
                return 
            val.append(nums[level])
            parse(val, level+1)
            val.pop()
            parse(val, level+1)

        parse([], 0)
        return res