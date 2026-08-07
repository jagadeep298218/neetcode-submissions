'''
helper method:
    amount of water --> min(h1, h2) * abs(indexof(h2)-indexof(h1))\

    2 pointer solution

'''


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        res = 0
        while left < right:
            res = max(res, self.amount(heights[left], heights[right], left, right))
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return res

    def amount(self, h1, h2, left, right):
        return min(h1, h2) * abs(left - right)
        