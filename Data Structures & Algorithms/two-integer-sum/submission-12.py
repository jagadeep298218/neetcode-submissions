class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}

        for ind, num in enumerate(nums):
            if target - num in check:
                return [check[target-num], ind]
            else:
                check[num] = ind
        return [0,0]