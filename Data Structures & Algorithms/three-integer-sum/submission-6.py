class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i, n in enumerate(nums):
            if i > 0 and (n == nums[i-1]):
                continue
            l = i+1
            r = len(nums)-1

            while l < r:
                Sum = n + nums[l] + nums[r]
                if Sum > 0:
                    r -= 1
                elif Sum < 0:
                    l += 1
                else:
                    result.append([n, nums[l], nums[r]])
                    l += 1
                    while (nums[l-1] == nums[l])  and (l < r):
                        l+= 1
        return result

                