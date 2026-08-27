class Solution:
    def validPalindrome(self, s: str) -> bool:
        '''
        abbda
         - -
        '''

        left, right = 0, len(s)-1
        check = False
        def run(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l +=1 
                r -= 1
            return True

        while left < right:
            if s[left] == s[right]:
                left+=1 
                right-=1 
            else:
                break
        
        return (run(left+1, right) or run(left, right-1))
        
                