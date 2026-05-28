class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lookup = [["(",")"], ["[", "]"], ["{", "}"]]



        for char in s:
            if (len(stack) != 0) and [stack[-1], char] in lookup:
                stack.pop()
            else:
                stack.append(char)
        
        if len(stack) == 0:
            return True
        
        else:
            return False