class Solution:
    def isPalindrome(self, s: str) -> bool:
        sl = s.lower()

        left, right = 0, len(s)-1

        while left < right:
            while left < right and not sl[left].isalnum():
                left+=1
            while left < right and not sl[right].isalnum():
                right -= 1
            if sl[left] != sl[right]:
                return False
            left += 1
            right -= 1
        return True