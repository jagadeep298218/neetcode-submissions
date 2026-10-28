class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = [0] * len(height)
        right_max = [0] * len(height)

        right, left = 0, 0

        for i in range(len(height)):
            left = max(left, height[i])
            right = max(right, height[len(height)-i-1])
            left_max[i] = left
            right_max[i] =right
            
        res = 0
        right_max = right_max[::-1]
        for i in range(len(height)):
            res += (min(left_max[i], right_max[i]) - height[i])
        return res