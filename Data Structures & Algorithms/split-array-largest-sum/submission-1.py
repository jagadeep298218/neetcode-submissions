class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        

        def check(mid):
            check_k = 1
            total = 0
            for num in nums:
                if total + num > mid:
                    total = 0
                    check_k+= 1
                total += num
            return check_k

        left = max(nums)
        right = sum(nums)
        res = -1
        while left <= right:
            mid = (left+right)//2
            check_k = check(mid)
            if check_k <= k:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res
            