class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def parse(val, open, close):
            if (open + close) == (n*2):
                if open == close:
                    res.append(val)
                return 
            parse(val + "(", open+1, close)
            if close < open:
                parse(val+")", open, close+1)

        parse("", 0, 0)
        return res