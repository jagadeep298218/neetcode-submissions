class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        store running sum?
        2 -1 1 2
        1
        
        '''
        hashim = {}
        hashim[0] = 1
        res = 0
        pre = 0
        for num in nums:
            pre += num
            if (pre - k) in hashim:
                res += hashim[pre - k]
            
            hashim[pre] = hashim.get(pre, 0) + 1
        
        return res