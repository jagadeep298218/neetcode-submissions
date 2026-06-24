class Solution:
    def canPartition(self, nums: List[int]) -> bool:  
        target = 0
        for i in nums:
            target += i
        if target%2 == 1: return False
        target /= 2

        sums = set()
        sums.add(0)
        for i in range(len(nums)-1,0,-1):
            arr = []
            for j in sums:
                arr.append(nums[i] + j)
            for j in arr:
                sums.add(j)
            if target in sums:
                return True
        
        return False
