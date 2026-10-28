class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # prefix sum
        prefix = [0] * (len(nums)+1)
        total = 0
        for index, num in enumerate(nums):
            total += num
            prefix[index+1] = total
        hash = {}
        res = 0
        for num in prefix:
            if (num-k) in hash:
                res += hash[(num-k)]
            hash[(num)] = hash.get((num), 0) + 1
        
        return res
