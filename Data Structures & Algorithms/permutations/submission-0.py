class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def parse(val, level):
            if level == len(nums):
                cal_copy = val.copy()
                res.append(cal_copy)
                return 
            for i in range(len(nums)):
                if nums[i] not in val:
                    val.append(nums[i])
                    parse(val, level+1)
                    val.pop()

        parse([], 0)
        return res