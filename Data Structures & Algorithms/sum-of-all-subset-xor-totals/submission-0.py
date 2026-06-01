class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.res = 0

        def XOR(subset):
            val = 0
            for x in subset:
                val ^= x
            self.res += val

        def parse(i, current):
            if i == len(nums):
                XOR(current)
                return
            parse(i + 1, current)   
            parse(i + 1, current + [nums[i]]) 

        parse(0, [])
        return self.res