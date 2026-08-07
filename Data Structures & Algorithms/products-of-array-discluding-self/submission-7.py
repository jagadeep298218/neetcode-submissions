class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        case, prod = 1, 1

        for num in nums:
            if num == 0 and case == 2:
                case = 3
                break
            elif num == 0:
                case = 2
            else:
                prod *= num
        
        if case == 3:
            return ([0] * len(nums))
        res = []
        if case == 2:
            for i in range(len(nums)):
                if nums[i] == 0:
                    res.append(prod)
                else:
                    res.append(0)
            return res
        for i in range(len(nums)):
            res.append(int(prod/nums[i]))
        
        return res
        
        
