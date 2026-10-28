class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        stack = []
        res = [0] * n

        for ind in range(n-1, -1, -1):
            while stack and (heights[ind] > heights[stack[-1]]):
                res[ind] += 1
                stack.pop()
            if stack:
                res[ind] += 1
            stack.append(ind)
        return res