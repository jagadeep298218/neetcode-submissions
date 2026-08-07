class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        chars = set(s[0])
        max_res = 1

        left, right = 0, 1
        res = 1
        while left < right and (right < len(s)):

            while s[right] in chars:
                chars.remove(s[left])
                left += 1

            chars.add(s[right])
            right += 1
            max_res = max(max_res, right-left)
        return max_res
            

