class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sets = {}

        for i in range(len(nums)):
            if nums[i] in sets:
                return [sets[nums[i]], i]
            else: 
                sets[(target-nums[i])] = i;
        

        return [0,0]