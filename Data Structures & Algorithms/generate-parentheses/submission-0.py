class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def check(val):
            stack = []
            for i in range(len(val)):
                if not stack and val[i]==")":
                    return False
                elif val[i]==")":
                    stack.pop()
                else: stack.append("(")
            if len(stack) == 0:
                return True
            else: return False

        def parse(val, level):
            if level == (n*2):
                if check(val): 
                    res.append(val)
                    return 
                else: return 
            parse(val+"(", level+1)
            parse(val+")", level+1)

        parse("", 0)
        return res