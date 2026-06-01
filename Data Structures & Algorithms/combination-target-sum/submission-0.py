class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []
        sol = []

        def parse(i, total):
            if total == target:
                self.res.append(sol[:])
                return
            if total > target or i == len(nums):
                return

            sol.append(nums[i])
            parse(i, total + nums[i])    # reuse same element
            sol.pop()

            parse(i + 1, total)          # skip element

        parse(0, 0)
        return self.res