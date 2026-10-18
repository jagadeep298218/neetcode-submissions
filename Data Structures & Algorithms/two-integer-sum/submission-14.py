class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        map = {}

        for index, num in enumerate(nums):
            if num in map:
                return [map[num], index]
            map[target - num] = index
        return [-1, -1]

        
        