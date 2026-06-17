class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, val in enumerate(temperatures):
            while stack and val > stack[-1][0]:
                x, y = stack.pop()
                res[y] = i - y
            stack.append((val, i))
        
        return res
