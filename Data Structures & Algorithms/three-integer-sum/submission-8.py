'''
hashMap -->
-1 : [0, 1]
0 : [0, 2]...

sort triplets --> [-1, 0, -1] : [-1, -1, 0]

[0, 2, 2, 3, 4]

time -> ON^2
space -> ON^2 + k where k is the resulting number of triplets
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        checked = set()
        res = []
        for i in range(len(nums)):
            if nums[i] in checked:
                continue
            checked.add(nums[i])
            left, right = i+1, len(nums)-1
            
            while left < right:
                s = nums[left] + nums[right]
                if s == -nums[i]:
                    if [nums[i], nums[left], nums[right]] not in res:
                        res.append([nums[i], nums[left], nums[right]])
                    left += 1
                elif s > -nums[i]:
                    right -= 1
                else:
                    left += 1

        return res




